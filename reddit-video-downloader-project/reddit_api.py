import customtkinter as ctk
from tkinter import filedialog
import os
import subprocess
from dotenv import load_dotenv
import praw
import re

load_dotenv()

# Variables:
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
password = os.getenv('PASSWORD')
username = os.getenv('REDDIT_USERNAME')
subreddits = ['unexpected', 'PublicFreakout', 'InstantRegret', 'holdmyjuicebox']
sortby = ['new', 'hot', "best", "top", "rising"]
save_location = ""
info = ""

# Reddit info:
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password=password,
    username=username,
    user_agent='personal use script'
)

# remove invlaid characters:
def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)

# Select location to save files:
def choose_save_location():
    global save_location
    selected_folder = filedialog.askdirectory(
        title="Select folder to save files"
    )
    if selected_folder:
        save_location = selected_folder
        save_label.configure(text=f"Save location: {save_location}")

# Download files function:
def download_files():
    global save_location
    if not save_location:
        info_label.configure(text="Please select a save location first.")
        return

    sub_select = subselect.get()
    sort_select = sortselect.get().lower()
    num_select = numselect.get()

    try:
        num_select = int(num_select)
        if num_select <= 0:
            raise ValueError
    except ValueError:
        info_label.configure(text="Please enter a valid positive number.")
        return

    subreddit = reddit.subreddit(sub_select)
    posts = getattr(subreddit, sort_select)(limit=num_select)

    for post in posts:
        if post.media and "reddit_video" in post.media:
            reddit_post_url = f"https://www.reddit.com{post.permalink}"
            safe_title = sanitize_filename(post.title)
            output_filename = f"{safe_title}.mp4"
            full_path = os.path.join(save_location, output_filename)

            info_label.configure(text=f"Downloading: {post.title}")
            window.update_idletasks()

            yt_dlp_command = [
                "yt-dlp",
                "-f", "bestvideo+bestaudio",
                "--merge-output-format", "mp4",
                "-o", full_path,
                reddit_post_url
            ]
            subprocess.run(yt_dlp_command)

    info_label.configure(text="All downloads complete.")

# Create the window:
window = ctk.CTk()
window.geometry("400x550")
window.title("Reddit Video Downloader")

# Select Subreddit:
sub_title = ctk.CTkLabel(window, text="Select a Subreddit", font=("Helvetica", 16))
sub_title.pack(pady=10)
subselect = ctk.CTkComboBox(window, values=subreddits)
subselect.pack(pady=5)

# Select Sort By:
sort_title = ctk.CTkLabel(window, text="Sort by...", font=("Helvetica", 16))
sort_title.pack(pady=10)
sortselect = ctk.CTkComboBox(window, values=sortby)
sortselect.pack(pady=5)

# Select number of posts:
num_title = ctk.CTkLabel(window, text="Enter number of posts", font=("Helvetica", 16))
num_title.pack(pady=10)
numselect = ctk.CTkEntry(window, placeholder_text="Enter number of posts", width=50, height=20)
numselect.pack(pady=5)

# Select save location:
save_title = ctk.CTkLabel(window, text="Select save location...", font=("Helvetica", 16))
save_title.pack(pady=10)
savebutton = ctk.CTkButton(window, text="Choose Folder", command=choose_save_location)
savebutton.pack(pady=5)

# Show info on current save location
save_label = ctk.CTkLabel(window, text="No folder selected", font=("Helvetica", 12))
save_label.pack(pady=5)

# Download files:
download_button = ctk.CTkButton(window, text="Download Files", command=download_files)
download_button.pack(pady=20)

# Dynamic information label:
info_label = ctk.CTkLabel(window, text=info, font=("Helvetica", 14))
info_label.pack(pady=10)

window.mainloop()