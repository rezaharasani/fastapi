import logging
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from .routers import user, post, auth, vote
from .tracing_middleware import TraceRequestBodyMiddleware, TraceResponseBodyMiddleware

""" Notice:
Our database will be created automatically by alembic.
The following method is used to initialize database by manual way."""
from . import models
from .database import engine
from .config import settings

models.Base.metadata.create_all(bind=engine)

# --- Logging Setup with Correlation ---
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s %(levelname)s [trace_id=%(otelTraceID)s span_id=%(otelSpanID)s] %(message)s",
# )
# logger = logging.getLogger("app")
# LoggingInstrumentor().instrument(set_logging_format=True)

# --- OpenTelemetry Setup ---
resource = Resource.create({"service.name": "fastapi-app"})
provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)

# --- OTLP Exporter ---
otlp_exporter = OTLPSpanExporter(
    endpoint="http://jaeger:4317",
    insecure=True
)
span_processor = BatchSpanProcessor(otlp_exporter)
provider.add_span_processor(span_processor)

# --- Instrumentation AFTER setting provider ---
HTTPXClientInstrumentor().instrument()

app = FastAPI(
    title="FastAPI",
    description=f"Python and FastAPI Project in {settings.ENVIRONMENT.title()} Mode",
    version=f"{settings.PROJECT_VERSION}",
    docs_url="/docs",
    redoc_url="/redoc",
    root_path="/api/v1",
    deprecated=False
)
FastAPIInstrumentor().instrument_app(app)

tracer = trace.get_tracer(__name__)

# This is used for capturing content body of HTTP request and response.
# Be careful, in real production environment, you should not use this.
app.add_middleware(TraceRequestBodyMiddleware)
# app.add_middleware(TraceResponseBodyMiddleware)
#
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

app.include_router(user.router)
app.include_router(post.router)
app.include_router(vote.router)
app.include_router(auth.router)


@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return {"message": "Welcome to the FastAPI project."}


@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "healthy"}
