# Job Search Script in Python

## Overview
This script helps users find job listings using the Adzuna API. It automatically installs required dependencies and retrieves job information based on the user's chosen industry.

## Secure API Credentials
Sensitive details like API keys are stored in a `.env` file instead of being hardcoded in the script. This prevents accidental exposure.

### Create a `.env` File
1. Create a file named `.env` in the same directory as the script.
2. Add the following:

API_KEY = your_api_key_here

APP_ID = your_app_id_here

ROOT_URL = "https://api.adzuna.com/v1/api/jobs/gb/search/1"

3. Save the file.

## How It Works
1. Ensures necessary packages are installed (`httpx`, `python-dotenv`).
2. Loads API credentials from the `.env` file securely.
3. Prompts the user to enter a job industry.
4. Fetches matching job listings using the Adzuna API.
5. Displays job details, including title, company, salary, and application link.
6. Allows users to repeat the search process until they choose to exit.

## Running the Script
To execute the script, run it in a Python environment and follow the prompts to search for jobs.

This approach keeps sensitive information secure while providing an efficient way to explore job opportunities.