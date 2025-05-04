from langflow.interface.base import Tool
from task_queue.tasks.post_linkedin import post_to_linkedin_task

class LinkedInPostNode(Tool):
    name = "Post to LinkedIn"
    description = "Send a job to the LinkedIn Celery queue"

    def build(self, job: dict) -> str:
        post_to_linkedin_task.delay(job)
        return " LinkedIn task dispatched"
