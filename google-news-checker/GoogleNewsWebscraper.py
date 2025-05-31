import subprocess
import sys
import importlib
import requests
from bs4 import BeautifulSoup

# Install dependencies if missing
def install_packages():
    required_packages = ["requests", "beautifulsoup4", "lxml", "datetime"]
    for package in required_packages:
        try:
            importlib.import_module(package.replace("-", "_"))
        except ImportError:
            print(f"Installing missing package: {package}")
            subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)

install_packages()

from datetime import datetime

# Define variables:
url = 'https://news.sky.com/topic/chile-6421'

# Fetch the page content
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

# Extract articles
articles = soup.find_all("article")

# Loop through results:
for idx, article in enumerate(articles, start=1):
    # Define headline and timestamp variables:
    headline = article.find("a")  # Adjust this if needed
    timestamp = article.find("time")

    # If the headline field has information...:
    if headline:
        headline_text = headline.text.strip()
    # If there is no headline info...:
    else:
        headline_text = "No headline found"

    if timestamp and timestamp.has_attr("datetime"):
        original_date = timestamp["datetime"]  # Full timestamp (YYYY-MM-DD HH:MM:SS)
        formatted_date = datetime.strptime(original_date, "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")  # Convert to DD-MM-YYYY
    else:
        formatted_date = "No date available"

    # Print the results to terminal
    print(f"{idx}. {formatted_date} - {headline_text}")