# Use subprocess to chec for requests python-dotenv:
import subprocess
import sys

# Install dependencies if missing
def install_packages():
    required_packages = ["requests", "python-dotenv"]
    for package in required_packages:
        subprocess.run([sys.executable, "-m", "pip", "install", package])

install_packages()
# Access environment variables:
import os
# Make HTTP requests:
import requests
# Load the .env file:
from dotenv import load_dotenv

load_dotenv()

# Define the weather checking function:
def get_weather(city):
    api_key = os.getenv("OWM_API_KEY")
    # If it doesn't find the APi key....
    if not api_key:
        # Print the following error message and exit:
        print("API key not found. Please set this in the .env file.")
        return
    # Build the URL for the request by imputting the city name and the API key:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        # Send the HTTP GET request to openweathermap.org...
        response = requests.get(url)
        # Responds with Python error if needed:
        response.raise_for_status()
        # Converts the response from website to JSON:
        data = response.json()

        # Gets weather info from the response:
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Print results:
        print(f"\n Weather in {city.title()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {description.title()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

    # Error handling:
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error: {req_err}")
    except KeyError:
        print("Unexpected response format. Check city name and API key.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Rin the script prompting city to be input:
if __name__ == "__main__":      # Ensure this is not being run form a module
    city = input("Enter city name: ")       # Input city name as variable.
    get_weather(city)       # Start the script using city name variable.