import os
import sys
from tqdm import tqdm
import time
import importlib
import subprocess
import json

def require_packages():
    packages = [ "httpx", "python-dotenv" ]
    for package in tqdm(packages, desc = "Checking for required packages..."):
        import_name = "dotenv" if package == "python-dotenv" else package
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
    time.sleep(3)
    if os.name == 'nt':
        os.system('cls')
    else: os.system('clear')

require_packages()

import httpx
from dotenv import load_dotenv
load_dotenv()

def octopus_tariffs():
    post_code = os.getenv("post_code").replace(" ", "")
    r = httpx.get(f"https://api.octopus.energy/v1/products/?postcode={post_code}")
    r.raise_for_status
    data = r.json()
    
    for tariff in data['results']:
        name = tariff.get('display_name')
        code = tariff.get('code')
        available_from = tariff.get('available_from')
        print(name)
        print(code)
        print(available_from)
        
        print("-" * 60)

octopus_tariffs()