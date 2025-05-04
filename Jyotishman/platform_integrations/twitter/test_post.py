from adapter import post_to_twitter

sample_job = {
    "Job_Title": "Full Stack Engineer",
    "Location": "Remote",
    "Skills": ["React", "Node.js", "AWS"]
}

post_to_twitter(sample_job)
