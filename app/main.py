from fastapi import FastAPI
from app.core.logging import setup_logging
import logging

setup_logging()

logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
async def health_check():
    logger.info("Health check endpoint called....")
    return {"status": "ok"}