# adapter.py — Telegram Job Posting Formatter & Mock

def format_for_telegram(job):
    return f"""
 *{job['Job_Title']}*
 _Location_: {job['Location']}
 _Skills_: {', '.join(job['Skills'])}

We are hiring! Join us and make an impact.

#hiring #{job['Job_Title'].replace(' ', '')}
""".strip()

def post_to_telegram(job):
    formatted = format_for_telegram(job)
    print("Simulating Telegram post...")
    print(formatted)
