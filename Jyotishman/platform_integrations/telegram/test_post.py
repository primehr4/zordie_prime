from adapter import post_to_telegram

sample_job = {
    "Job_Title": "Marketing Specialist",
    "Location": "Remote",
    "Skills": ["SEO", "Google Ads", "Analytics"]
}

post_to_telegram(sample_job)
