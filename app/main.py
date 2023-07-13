from fastapi import FastAPI
from api.endpoints import router
from core.event_handlers import subscribe_event_handlers

app = FastAPI()

app.include_router(router)

subscribe_event_handlers()
