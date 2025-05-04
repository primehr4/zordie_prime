from task_queue.tasks.post_task import post_to_twitter_task

sample_job = {
    "Job_Title": "Full Stack Engineer",
    "Location": "Remote",
    "Skills": ["React", "Node.js", "AWS"]
}

post_to_twitter_task.delay(sample_job)
