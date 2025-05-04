from langflow.interface.base import Tool
from task_queue.tasks.post_telegram import post_to_telegram_task

class TelegramPostNode(Tool):
    name = "Post to Telegram"
    description = "Send a job to the Telegram Celery queue"

    def build(self, job: dict) -> str:
        post_to_telegram_task.delay(job)
        return " Telegram task dispatched"
