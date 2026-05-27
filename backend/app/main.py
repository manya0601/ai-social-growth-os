from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.tasks import router as task_router
from app.api.memory import router as memory_router
from app.api.retrieval import router as retrieval_router
from app.api.competitors import router as competitor_router

app = FastAPI(
    title="AI Social Growth OS",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(task_router)
app.include_router(memory_router)
app.include_router(retrieval_router)
app.include_router(competitor_router)

@app.get("/")
async def root():
    return {
        "message": "AI Social Growth OS Backend Running"
    }