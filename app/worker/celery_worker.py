from celery import Celery

celery_app = Celery(
    "docgen_worker", broker="redis://redis:6379/0", backend="redis://redis:6379/0"
)

celery_app.conf.task_routes = {
    "app.tasks.jobs.generate_documentation_task": {"queue": "docgen"},
}
