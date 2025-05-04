from celery import shared_task
# from task_queue.celery_config.celery_app import app
# from platform_integrations.telegram.adapter import post_to_telegram

# @app.task(bind=True, max_retries=3, default_retry_delay=5)
# def post_to_telegram_task(self, job):
#     try:
#         post_to_telegram(job)
#         return "Telegram post successful"
#     except Exception as e:
#         print("Telegram post failed. Retrying...")
#         raise self.retry(exc=e)

import logging
from task_queue.celery_config.celery_app import app
from platform_integrations.telegram.adapter import post_to_telegram
from common.logging.logger import setup_logger

telegram_logger = setup_logger("telegram", "telegram.log")

@app.task(bind=True, max_retries=3, default_retry_delay=5)
def post_to_telegram_task(self, job):
    try:
        post_to_telegram(job)
        telegram_logger.info(f" Successfully posted: {job}")
        for handler in telegram_logger.handlers:
            if isinstance(handler, logging.FileHandler):
                handler.flush()
        return "Telegram post successful"
    except Exception as e:
        telegram_logger.error(f" Failed to post: {job} | Error: {str(e)}")
        raise self.retry(exc=e)

