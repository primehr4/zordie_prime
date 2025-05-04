# task_queue/tasks/post_linkedin.py

# from task_queue.celery_config.celery_app import app
# from platform_integrations.linkedin.adapter import post_to_linkedin

# @app.task
# def post_to_linkedin_task(job):
#     post_to_linkedin(job)
#     return "LinkedIn post successful"

from celery import shared_task
# from task_queue.celery_config.celery_app import app
# from platform_integrations.linkedin.adapter import post_to_linkedin

# @app.task(bind=True, max_retries=3, default_retry_delay=5)
# def post_to_linkedin_task(self, job):
#     try:
#         post_to_linkedin(job)
#         return "LinkedIn post successful"
#     except Exception as e:
#         print("LinkedIn post failed. Retrying...")
#         raise self.retry(exc=e)

import logging
from task_queue.celery_config.celery_app import app
from platform_integrations.linkedin.adapter import post_to_linkedin
from common.logging.logger import setup_logger

linkedin_logger = setup_logger("linkedin", "linkedin.log")

@app.task(bind=True, max_retries=3, default_retry_delay=5)
def post_to_linkedin_task(self, job):
    try:
        post_to_linkedin(job)
        linkedin_logger.info(f" Successfully posted: {job}")
        for handler in linkedin_logger.handlers:
            if isinstance(handler, logging.FileHandler):
                handler.flush()
        return "LinkedIn post successful"
    except Exception as e:
        linkedin_logger.error(f" Failed to post: {job} | Error: {str(e)}")
        raise self.retry(exc=e)

