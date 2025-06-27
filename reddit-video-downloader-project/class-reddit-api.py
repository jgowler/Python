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

class App(ctk.CTk):
    def __init__(self, title, geometry, client_id, client_secret, password, username):
        super().__init__()
        global reddit
        # Create the window:
        self.title(title)
        self.geometry(f'{geometry[0]}x{geometry[1]}')
        # Select Subreddit:
        self.sub_title = ctk.CTkLabel(self, text="Select a Subreddit", font=("Helvetica", 16))
        self.sub_title.pack(pady=10)
        self.subselect = ctk.CTkComboBox(self, values=subreddits)
        self.subselect.pack(pady=5)
        # Select Sort By:
        self.sort_title = ctk.CTkLabel(self, text="Sort by...", font=("Helvetica", 16))
        self.sort_title.pack(pady=10)
        self.sortselect = ctk.CTkComboBox(self, values=sortby)
        self.sortselect.pack(pady=5)

        # Select number of posts:
        self.num_title = ctk.CTkLabel(self, text="Enter number of posts", font=("Helvetica", 16))
        self.num_title.pack(pady=10)
        self.numselect = ctk.CTkEntry(self, placeholder_text="Enter number of posts", width=50, height=20)
        self.numselect.pack(pady=5)

        # Select save location:
        self.save_title = ctk.CTkLabel(self, text="Select save location...", font=("Helvetica", 16))
        self.save_title.pack(pady=10)
        self.savebutton = ctk.CTkButton(self, text="Choose Folder", command=self.choose_save_location)
        self.savebutton.pack(pady=5)

        # Show info on current save location
        self.save_label = ctk.CTkLabel(self, text="No folder selected", font=("Helvetica", 12))
        self.save_label.pack(pady=5)

        # Download files:
        self.download_button = ctk.CTkButton(self, text="Download Files", command=self.download_files)
        self.download_button.pack(pady=20)

        # Dynamic information label:
        self.info_label = ctk.CTkLabel(self, text=info, font=("Helvetica", 14))
        self.info_label.pack(pady=10)

    def sanitize_filename(self, filename):
        return re.sub(r'[\\/*?:"<>|]', "", filename)

    def choose_save_location(self):
        global save_location
        selected_folder = filedialog.askdirectory(
            title = "Select folder to save files to"
        )
        if selected_folder:
            save_location = selected_folder
            self.save_label.configure(text = f"Save location: {save_location}")
    
    def download_files(self):
        global save_location
        if not save_location:
            self.info_label.configure(text = "Please select a save location first.")
            return
        
        sub_select = self.subselect.get()
        sort_select = self.sortselect.get().lower()
        num_select = self.numselect.get()

        try:
            num_select = int(num_select)
            if num_select <= 0:
                raise ValueError
        except ValueError:
            self.info_label.configure(text="Please enter a valid positive number.")
            return
    
        subreddit = reddit.subreddit(sub_select)
        posts = getattr(subreddit, sort_select)(limit=num_select)

        for post in posts:
            if post.media and "reddit_video" in post.media:
                reddit_post_url = f"https://www.reddit.com{post.permalink}"
                save_title = self.sanitize_filename(post.title)
                output_filename = f"{save_title}.mp4"
                full_path = os.path.join(save_location, output_filename)

                self.info_label.configure(text=f"Downloading: {post.title}")
                self.update_idletasks()

                ffmpeg_path = os.path.join("tools", "ffmpeg.exe")
                output_template = os.path.join(save_location, f"{save_title}.%(ext)s")
                yt_dlp_command = [
                    "yt-dlp",
                    "--ffmpeg-location", os.path.dirname(ffmpeg_path),
                    "-f", "bestvideo+bestaudio",
                    "--merge-output-format", "mp4",
                    "-o", output_template,
                    reddit_post_url
                ]
                subprocess.run(yt_dlp_command)
            self.info_label.configure(text = "Download complete.")



App('test-window', (600, 500), client_id, client_secret, password, username).mainloop()

