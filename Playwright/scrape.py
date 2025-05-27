import time
import os
import sys
import subprocess
from dotenv import load_dotenv # Load .env file variables
from playwright.sync_api import sync_playwright, Playwright
from datetime import datetime # Import Date/Time info
from tqdm import tqdm # Used to create a progress bar as browser will run headless.

# Install all required packages if not present. Will not do anything if already installed:
def required_packages():
    required_packages = ['pytest-playwright', 'python-dotenv', 'tqdm']
    for package in required_packages:
        subprocess.run([sys.executable, "-m", "pip", "install", package])
        print(f"Installing {package}")

# Define a function to clear the screen once the required_packages function has run:
def clear_screen():
    if os.name == "nt": # Windows
        os.system("cls")
    else: # Linux, Mac
        os.system("clear")

required_packages()
load_dotenv()

# Variables:
today_date = datetime.now().strftime("%d-%m-%Y")
download_folder = os.getenv('doc_location')
url = os.getenv("url")
bill_numbers = [num.strip() for num in os.getenv("bill_numbers", "").split(",")]

# Set up Playwright to open browser headless and accept downloads automatically:
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, slow_mo=50)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    clear_screen()
    
    # For each of the bills specified in the .env file...:
    for bill in tqdm(bill_numbers, desc="Downloading bills..."):
        filename = f"{bill}_{today_date}.xlsx"
        filepath = os.path.join(download_folder, filename)

        # Go to the website...
        page.goto(url)
        
        # Perform the following actions...:
        page.fill('input#txtNBoletin', bill)
        page.press('input#txtNBoletin', 'Enter')
        # Wait for the page to load. This can be determined by the network going idle as page will be loaded:
        page.wait_for_load_state('networkidle')
        # Click the button on the site to initiate the document download:
        page.click('button#btnExcel')

        # Set up the download location:
        with page.expect_download() as download_info:
            download = download_info.value
            download.save_as(filepath)
