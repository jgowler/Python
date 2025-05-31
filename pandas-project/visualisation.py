import os
import sys
import subprocess
import datetime
import pandas as pd
import json
import importlib
import time
import matplotlib.pyplot as plt
import seaborn as sns

# Create function to clear screen depending on OS:
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Create function to check required packages are installe don system:
def required_packages():
    rp = [ 'httpx', 'python-dotenv', 'seaborn', 'matplotlib' ]
    for p in rp:
        import_name = 'dotenv' if p == 'python-dotenv' else p
        try:
            importlib.import_module(import_name)
        except ImportError:
            print(f"{p} is not installed. Installing...")
            subprocess.run(
                [sys.executable, "-m", "pip", "install", p],
                stderr=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL
                )
    clear_screen()

required_packages()
import httpx
from dotenv import load_dotenv
load_dotenv()

# Variables:

API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')

# Create params for GET request:
params = {
    'apikey': API_KEY,
    'function': 'TOP_GAINERS_LOSERS',
    'datatype': 'json'
}

# Create function to run the GET request and get info on global stock market:
def gainers_losers():
    with httpx.Client() as client:
        rc = client.get(BASE_URL, params=params)
        if rc.status_code != 200:
            print(f"Error: Status code {rc.status_code}")
            sys.exit()
        results = rc.json()
        tidy = json.dumps(results, indent=4)
        print(tidy)
        #return results
# Create function to sort the gainers from the results of gainers_losers:
def gainers(results):
    return sorted(
        results.get("top_gainers", []),
            key = lambda x: float(x.get('price', 0)),
            reverse = True
        )
# Create function to sort the losers from the results of gainers_losers:
def losers(results):
    return sorted(
            results.get("top_losers", []),
            key = lambda x: float(x.get("price", 0)),
            reverse = True
        )
# Create function to sort the most active from the results of gainers_losers:
def most_active(results):
    return sorted(
            results.get("most_actively_traded", []),
            key = lambda x: float(x.get("volume", 0)),
            reverse = True
        )
# Create function to visualise the gainers:
def visualise_gainers(sorted_gainers):
    if not sorted_gainers:
        print("No gainers data to visualize.")
        return
    
    df = pd.DataFrame(sorted_gainers)
    print("DataFrame columns for gainers:", df.columns.tolist())  # Debug print

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    
    plt.title("Top Gainers by Volume")
    plt.xlabel("Ticker")
    plt.ylabel("Volume")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Create function to visualise the losers:
def visualise_losers(sorted_losers):
    if not sorted_losers:
        print("No losers data to visualize.")
        return

    df = pd.DataFrame(sorted_losers)
    print("DataFrame columns for losers:", df.columns.tolist())  # Debug print

    sns.set_theme(style='whitegrid')
    plt.figure(figsize=(10, 6))

    plt.title("Top Losers by Volume")
    plt.xlabel("Ticker")
    plt.ylabel("Volume")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Create function to visualise the most active:
def visualise_most_active(sorted_most_active):
    if not sorted_most_active:
        print("No most active data to visualize.")
        return

    df = pd.DataFrame(sorted_most_active)
    print("DataFrame columns for most active:", df.columns.tolist())  # Debug print

    sns.set_theme(style='whitegrid')
    plt.figure(figsize=(10, 6))

    plt.title("Most Actively Traded Stocks by Volume")
    plt.xlabel("Ticker")
    plt.ylabel("Volume")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

'''
    Request to API works, issue is no data is retrieved for price an volume to be visualised. review changes
'''