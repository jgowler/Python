import sys
import os
import subprocess
import importlib
import praw
from urllib.parse import urlparse
from dotenv import load_dotenv


# Download required libraries
def required_packages():
    rp = ['python-dotenv', 'yt-dlp']
    for p in rp:
        import_name = 'dotenv' if p == 'python-dotenv' else p
        try:
            importlib.import_module(import_name)
        except ImportError:
            print(f"{p} was not found. Installing...")
            subprocess.run([sys.executable, "-m", "pip", "install", p])

required_packages()

load_dotenv()

# Reddit API creds:
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
password = os.getenv('PASSWORD')
username = os.getenv('REDDIT_USERNAME')

# Reddit info:
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password=password,
    username=username,
    user_agent='personal use script'
)

# Select subreddit:
subreddit = reddit.subreddit('unexpected')
# Select Top 10 of the above subreddit:
top_posts = subreddit.new(limit=10)

# For each post in the top 10...:
for post in top_posts:
    # If the post has media...:
    if post.media and "reddit_video" in post.media:
        reddit_post_url = f"https://www.reddit.com{post.permalink}"
        output_filename = f"{post.title}.mp4"

        print(f"Downloading: {post.title}")
        
        yt_dlp_command = [
            "yt-dlp",
            "-f", "bestvideo+bestaudio",
            "--merge-output-format", "mp4",
            "-o", output_filename,
            reddit_post_url
        ]

        subprocess.run(yt_dlp_command)

        print(f"Saved as: {output_filename}")
        print("-" * 60)
    else:
        print("No video posts found in the top 10.")