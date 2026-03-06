from app.core.config import settings
from fastapi import FastAPI
from app.core.logging import setup_logging
from prometheus_fastapi_instrumentator import Instrumentator
import logging
import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

if settings.sentry_dsn:
    sentry_sdk.init(dsn=settings.sentry_dsn, send_default_pii=True)

setup_logging()

logger = logging.getLogger(__name__)

app = FastAPI()

#Initializing the prometheus instrumentator
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

# Adding Sentry middleware to capture exceptions and performance data
app.add_middleware(SentryAsgiMiddleware)

@app.get("/")
async def root():
    logger.info("Root endpoint called....")
    return {"message": "Hello with FastAPI and Prometheus!"}

@app.get("/health")
async def health_check():
    logger.info("Health check endpoint called....")
    return {"status": "ok"}

@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0