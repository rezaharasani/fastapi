from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import user, post, auth, vote

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI",
    description="Python and FastAPI Project",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(user.router)
app.include_router(post.router)
app.include_router(vote.router)
app.include_router(auth.router)


@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    """Return greeting feedback"""
    return {"message": "Welcome to the FastAPI project."}


@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    """Health check"""
    return {"status": "healthy"}
