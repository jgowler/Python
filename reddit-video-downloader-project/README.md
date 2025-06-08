# Reddit Video Downloader with `yt-dlp`

This script downloads **video and audio files** from Reddit posts using `yt-dlp` and PRAW. The files are saved individually in the current working directory.

## PRAW Documents:
https://praw.readthedocs.io/en/stable/

## yt-dlp Documents:
https://github.com/yt-dlp/yt-dlp

## Features

- Fetches recent posts from a subreddit.
- Downloads video and audio separately.
- Saves files using the Reddit post title as the filename.
- Uses a `.env` file to store sensitive information.

## Prerequisites

Before running this script, install the following dependencies:

- [`praw`](https://praw.readthedocs.io/en/latest/) (**Must be installed manually**)

**The following will be downloaded automatically during the running of the script**
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)