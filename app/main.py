from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import user, post, auth, vote

""" Notice:
Our database will be created automatically by alembic.
The following method is used to initialize database by manual way."""
from . import models
from .database import engine
from .config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI",
    description="Python and FastAPI Project",
    version=f"{settings.PROJECT_VERSION}",
    docs_url="/docs",
    redoc_url="/redoc",
    root_path="/api/v1",
    deprecated=False
)

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


@app.get("/")
def root():
    return {"message": "welcome to my api"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
