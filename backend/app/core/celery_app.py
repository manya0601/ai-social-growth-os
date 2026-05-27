from celery import Celery

celery = Celery(
    "ai_social_growth_os",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery.conf.task_routes = {
    "app.workers.*": {"queue": "default"}
}