import os
import sys
import time
import importlib
import httpx
import subprocess


def install_packages():
    required_packages = ['httpx', 'python-dotenv']
    for package in required_packages:
        try:
            importlib.import_module(package.replace("-", "_"))
        except ImportError:
            print(f"Installing required package: {package}")
            subprocess.run([sys.executable, "-m", "pip", "install", package])

install_packages()

from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv("API_KEY")
OMDBURL = f"http://www.omdbapi.com/?apikey={API_KEY}"

def movie_search(movie):
    while True:
        try:
            r = httpx.get(f"{OMDBURL}&t={movie}")
            r.raise_for_status()
            data = r.json()
            title = (data['Title'])
            released = (data['Released'])
            genre = (data['Genre'])
            plot = (data['Plot'])

            os.system('cls')
            print(f"Title: {title}")
            print(f"Released: {released}")
            print(f"Genre: {genre}")
            print(f"Plot: {plot}")

        except httpx.HTTPError as http_er:
            print(f"HTTP Error: {http_er.request.url}")
        except httpx.InvalidURL as InvUrl:
            print(f"Invalid URL: {InvUrl}")

        while True:
            search_again = input("Would you like to find another movie?: ").strip().lower()
            if search_again == "yes":
                new_movie = input("Select a movie: ")
                movie_search(new_movie)
            elif search_again == "no":
                print("Exiting...")
                sys.exit()
            else:
                print("Invalid response. Please choose either 'yes' or 'no'." )

        


movie = input("Select a movie: ")
movie_search(movie)