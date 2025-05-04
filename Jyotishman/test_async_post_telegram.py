from task_queue.tasks.post_telegram import post_to_telegram_task

sample_job = {
    "Job_Title": "Marketing Specialist",
    "Location": "Remote",
    "Skills": ["SEO", "Google Ads", "Analytics"]
}

post_to_telegram_task.delay(sample_job)
