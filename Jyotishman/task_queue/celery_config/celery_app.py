# task_queue/celery_config/celery_app.py

from celery import Celery

app = Celery("zordie", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0")

app.conf.update(
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    timezone='UTC',
    enable_utc=True,
)

from task_queue.tasks import post_task
from task_queue.tasks import post_linkedin
from task_queue.tasks import post_telegram
