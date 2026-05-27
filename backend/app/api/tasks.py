from fastapi import APIRouter

from app.workers.trend_worker import analyze_trends

router = APIRouter()

@router.post("/analyze-trends")
async def run_trend_analysis():
    task = analyze_trends.delay()

    return {
        "task_id": task.id,
        "status": "queued"
    }