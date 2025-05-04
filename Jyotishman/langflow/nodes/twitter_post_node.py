from langflow.interface.base import Tool
from task_queue.tasks.post_task import post_to_twitter_task

class TwitterPostNode(Tool):
    name = "Post to Twitter"
    description = "Send a job to the Twitter Celery queue"

    def build(self, job: dict) -> str:
        post_to_twitter_task.delay(job)
        return " Twitter task dispatched"
