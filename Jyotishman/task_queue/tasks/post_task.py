# task_queue/tasks/post_task.py

# from task_queue.celery_config.celery_app import app
# from platform_integrations.twitter.adapter import post_to_twitter

# @app.task
# def post_to_twitter_task(job):
#     post_to_twitter(job)
#     return "Posted successfully"

from celery import shared_task
# from task_queue.celery_config.celery_app import app
# from platform_integrations.twitter.adapter import post_to_twitter

# @app.task(bind=True, max_retries=3, default_retry_delay=5)  # 5 seconds between retries
# def post_to_twitter_task(self, job):
#     try:
#         post_to_twitter(job)
#         return "Twitter post successful"
#     except Exception as e:
#         print("Twitter post failed. Retrying...")
#         raise self.retry(exc=e)

from task_queue.celery_config.celery_app import app
from platform_integrations.twitter.adapter import post_to_twitter
from common.logging.logger import setup_logger

twitter_logger = setup_logger("twitter", "twitter.log")

@app.task(bind=True, max_retries=3, default_retry_delay=5)
def post_to_twitter_task(self, job):
    try:
        post_to_twitter(job)
        twitter_logger.info(f" Successfully posted: {job}")
        return "Twitter post successful"
    except Exception as e:
        twitter_logger.error(f" Failed to post: {job} | Error: {e}")
        raise self.retry(exc=e)
