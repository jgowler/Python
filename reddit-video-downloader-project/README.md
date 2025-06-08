# Reddit Video Downloader with `yt-dlp`

This script downloads **video and audio separately** from Reddit posts using `yt-dlp` and PRAW. The files are saved individually and are **not merged**.

## Features

- Fetches recent posts from a subreddit.
- Downloads **best available video** and **best available audio** separately.
- Saves files using the Reddit post title as the filename.
- Uses a `.env` file to **securely store sensitive authentication details**.

## Prerequisites

Before running this script, install the following dependencies:

- [`praw`](https://praw.readthedocs.io/en/latest/) (**Must be installed manually**)
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)
