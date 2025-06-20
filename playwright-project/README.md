# Playwright-Based Data Retrieval Tool

This tool was developed as a project to deepen my understanding of Playwright and its potential as an alternative to APIs when a public API is not available. The script utilizes information provided in the `.env` file to verify a specified website and download the corresponding spreadsheet to a designated location on the local machine.

## How the Script Works

1. **Setup and Dependencies**  
   - Installs required packages (`pytest-playwright`, `python-dotenv`, `tqdm`) if they are not already installed.
   - All packages used during the development of this program can be found in the **"requirements.txt"** file
   - Loads environment variables from the `.env` file to retrieve necessary configurations.  

2. **Configuration**  
   - Defines essential variables such as the download folder, target URL, and bill numbers in the `.env` file.  
   - Initializes Playwright to run a Chromium browser in headless mode with automatic download handling.  

3. **Automation Process**  
   - Navigates to the specified website.  
   - Iterates through the bill numbers, filling out an input field and submitting the request.  
   - Waits for the page to fully load before initiating the download.  
   - Saves each downloaded spreadsheet with a filename containing the bill number and current date.  