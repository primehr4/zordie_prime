# adapter.py — LinkedIn Job Posting Formatter & Mock

def format_for_linkedin(job):
    description = f"""
 Job Title: {job['Job_Title']}
 Location: {job['Location']}
 Skills Required: {', '.join(job['Skills'])}

Summary:
We are seeking a highly motivated {job['Job_Title']} to join our team.
If you're passionate about innovation and impact, apply now!

#hiring #careers #{job['Job_Title'].replace(' ', '')}
"""
    return description.strip()

def post_to_linkedin(job):
    formatted = format_for_linkedin(job)
    print("Simulating LinkedIn post...")
    print(formatted)
