# adapter.py — Twitter platform mock post

def format_for_twitter(job):
    return f" {job['Job_Title']} at {job['Location']}!\nSkills: {', '.join(job['Skills'])}\nApply now!"

def post_to_twitter(job):
    tweet = format_for_twitter(job)
    print("Simulating Twitter post...")
    print(tweet)
