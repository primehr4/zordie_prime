from task_queue.tasks.post_linkedin import post_to_linkedin_task

sample_job = {
    "Job_Title": "AI Engineer",
    "Location": "Bangalore, India",
    "Skills": ["PyTorch", "ML Ops", "Cloud"]
}

post_to_linkedin_task.delay(sample_job)
