import os
import sys
import subprocess
import datetime
import time
import json
import importlib

# Create function to clear screen, regardless of OS:
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
# Create function to install necessary packages for script:
def required():
    rp = ['httpx', 'seaborn', 'pandas', 'matplotlib']
    for p in rp:
        try:
            # If unable to import module due to not being installed..
            importlib.import_module(p)
        except ImportError:
            print(f"Installing {p}")
            # Silently install the above packages:
            subprocess.run(
                [sys.executable, "-m", "pip", "install", p],
                stderr = subprocess.DEVNULL,
                stdout = subprocess.DEVNULL
            )
    clear_screen()

required()
import httpx
import seaborn as sns
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pylab as plt
load_dotenv()

# Variables:

URL = "https://www.cheapshark.com/api/1.0/deals?"

# Params set for search (Game is on sale, under $15, sorted by ammount saved):
params = {
    'onSale': True,
    'upperPrice': 15,
    'sortBy' : 'Savings'
}

# Create function to check for deals and return results:
def game_sales_checker():
    r = httpx.get(URL, params = params)
    # Convert the GET request response to JSON:
    data = r.json()
    # Tidy JSON for readability:
    tidy = json.dumps(data, indent=4)
    return data

# Convert the returned results of above function into a DataFrame using Pandas...:
df = pd.DataFrame(game_sales_checker())
# Sort the converted results and choose the top 10:
df = df.sort_values(by = 'savings', ascending = False).head(15)

# Create function to visualise the converted results into a graph:
def visualise_deals(df):
    plt.style.use('classic')
    # Create Displot graph:
    sns.displot(x = 'title', y = 'savings', data = df)
    # Rotate the tick labels to 45 degress:
    plt.xticks(rotation=45, horizontalalignment="right")
    # Tile of graph:
    plt.title("Steam Game Deals - Savings %")
    # Y axiz label:
    plt.ylabel("Savings (%)")
    # X axis label:
    plt.xlabel("Game Title")
    # Show created graph:
    plt.show()

# Call the function, passing the Pandas Dataframe into the function which is the converted data return from game_sales_checker:
visualise_deals(df)