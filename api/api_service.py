from fastapi import FastAPI
from api.routers import settings, config, oauth, health, logs

app = FastAPI(
    title="Plex Debrid API",
    version="3.0.0"
)

app.include_router(settings.router, prefix="/api")
app.include_router(config.router, prefix="/api")
app.include_router(oauth.router, prefix="/api")
app.include_router(health.router, prefix="/api")
app.include_router(logs.router, prefix="/api")
