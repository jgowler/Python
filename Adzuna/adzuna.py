import sys
import subprocess
import importlib
import time
import os
import json
from tqdm import tqdm

# Create a funtion to check for and install the necessary packages to run script:
def required_packages():
    packages = [ 'httpx', 'python-dotenv' ]
    for package in tqdm(packages, desc="Checking installed packages..."):
        import_name = 'dotenv' if package == 'python-dotenv' else package
        try:
            importlib.import_module(import_name)
        except ImportError:
            subprocess.run([sys.executable, "-m", "pip", "install", package],
                           check = True,
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL
                           )
            importlib.invalidate_caches()
            importlib.import_module(import_name)

required_packages()

import httpx
from dotenv import load_dotenv
load_dotenv()

# Create a function to search for jobs in Adzuna using an API key and a keyword:
def adzuna_search():
    api_key = os.getenv("API_KEY")
    app_id = os.getenv("APP_ID")
    root_url = os.getenv("ROOT_URL")
    industry = input("What sector are you looking to work in?: ")
    if not industry:
        print("No keywords enetered. Exiting...")
        return
    
    # Parameters:
    params = {
        "app_id": app_id,
        "app_key": api_key,
        "what": industry,
        "content-type": "application/json",
    }

    # Use HTTPX to GET info using the Adzuna API and the above parameters:
    r = httpx.get(root_url, params=params)
    if r.status_code != 200:
        print(f"Error! Status code {r.status_code}")
        return
    # Parse JSON info from GET request:
    data = r.json()
    results = data.get("results", [])

    if not results:
        print("No jobs found matching your search.")
        return

    for job in results:
        print(f"Title: {job.get('title')}")
        print(f"Company: {job.get('company', {}).get('display_name')}")
        print(f"Category: {job.get('category', {}).get('label')}")
        print(f"Location: {job.get('location', {}).get('display_name')}")
        print(f"Salary: £{job.get('salary_min')}")
        print(f"Description: {job.get('description')}")
        print(f"Apply here: {job.get('redirect_url')}")
        print("-" * 60)
# Option to loop back to another search:
while True:
    adzuna_search()
    print("Would you like to search again?: Y/N")
    again = input()
    if again.lower() != "y":
        print("Goodbye!")
        break