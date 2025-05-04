from adapter import post_to_linkedin

sample_job = {
    "Job_Title": "AI Engineer",
    "Location": "Bangalore, India",
    "Skills": ["PyTorch", "ML Ops", "Cloud"]
}

post_to_linkedin(sample_job)
