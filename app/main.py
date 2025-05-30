from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI Doc Generator")
app.include_router(router)

