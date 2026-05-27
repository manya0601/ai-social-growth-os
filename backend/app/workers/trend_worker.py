from app.core.celery_app import celery

@celery.task
def analyze_trends():
    print("Analyzing social media trends...")

    return {
        "status": "success",
        "message": "Trend analysis complete"
    }