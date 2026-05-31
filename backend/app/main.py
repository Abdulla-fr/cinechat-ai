"""Main FastAPI application"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from app.core.config import settings
from app.core.database import engine, Base
from app.api import routes
from app.websocket.manager import manager as ws_manager

logger = logging.getLogger(__name__)

# Create database tables
Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan context manager"""
    # Startup
    logger.info("Starting up CineChat AI Backend")
    yield
    # Shutdown
    logger.info("Shutting down CineChat AI Backend")
    await ws_manager.close_all()


app = FastAPI(
    title="CineChat AI API",
    description="Real-time AI chat for cinephiles",
    version="0.1.0",
    lifespan=lifespan,
)

# Middleware
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=settings.LOG_LEVEL,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


# Health check
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "version": "0.1.0",
    }


# Include routers
app.include_router(routes.auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(routes.users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(routes.chats.router, prefix="/api/v1/chats", tags=["chats"])
app.include_router(routes.messages.router, prefix="/api/v1/messages", tags=["messages"])
app.include_router(routes.ai.router, prefix="/api/v1/ai", tags=["ai"])
app.include_router(routes.websocket.router, tags=["websocket"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
