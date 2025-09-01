from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .routers import user, post, auth, vote

""" Notice:
Our database will be created automatically by alembic.
The following method is used to initialize database by manual way."""
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI",
    description=f"Python and FastAPI Project in {settings.ENVIRONMENT.title()} Mode",
    version=f"{settings.PROJECT_VERSION}",
    docs_url="/docs",
    redoc_url="/redoc",
    root_path="/api/v1",
    deprecated=False
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"message": "Welcome to the FastAPI project."}


@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "healthy"}
