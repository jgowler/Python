import time
import os
import sys
import subprocess
import re
from playwright.sync_api import sync_playwright, Playwright
from datetime import datetime # Import Date/Time info
from tkinter import filedialog # Import filedialogue
import customtkinter as ctk # Custom TKinter
from tqdm import tqdm # Used to create a progress bar as browser will run headless.
import threading # Allow app to run in the background
import os



# Define a function to clear the screen once the required_packages function has run:
def clear_screen():
    if os.name == "nt": # Windows
        os.system("cls")
    else: # Linux, Mac
        os.system("clear")

# Variables:
os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "0"
today_date = datetime.now().strftime("%d-%m-%Y")
url = "https://tramitacion.senado.cl/appsenado/templates/tramitacion/"
bill_numbers = ["14986-13","14509-13","15098-13","14649-13","14650-13","14698-13","14718-13","14737-13","14782-13","14815-13","14840-13","14906-13","14836-13","15361-13","15401-13","15660-13","15446-13","15725-13","14335-13","14643-03","14899-07","15075-03","15440-03","15638-15","15610-03","15762-03","14632-03","9914-11","15039-11","14668-11","15129-11","15414-11","15681-06","15429-11","14094-11","15850-11","15353-07","15766-03","14820-04","14561-19","15017-12","15577-07","15687-12","15749-12","15326-12","15763-12","14805-12","14767-03","14821-07","8197-07","15516-34","14944-03","15044-12"]
save_label = ""
count = len(bill_numbers)
prog = 0

### Functions:

# remove invalid characters:
def sanitise_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)

class BillsDownloaderApp:
    def __init__(self, bill_numbers, url, today_date):
        self.bill_numbers = bill_numbers
        self.url = url
        self.today_date = today_date
        self.save_location = None

        self.window = ctk.CTk()
        self.window.geometry("400x550")
        self.window.title("Bills Downloader")
        
        # Show info on current save location
        self.save_label = ctk.CTkLabel(self.window, text="No folder selected", font=("Helvetica", 12))
        self.save_label.pack(pady=5)
        # Select save location:
        self.save_title = ctk.CTkLabel(self.window, text="Select save location...", font=("Helvetica", 16))
        self.save_title.pack(pady=10)
        savebutton = ctk.CTkButton(self.window, text="Choose Folder", command=self.choose_save_location)
        savebutton.pack(pady=5)
        # List of bills:
        bill_title = ctk.CTkLabel(self.window, text="List of bills to be downloaded", font=("Helvetica", 16))
        bill_title.pack(pady=10)
        self.billselect = ctk.CTkComboBox(self.window, values=bill_numbers)
        self.billselect.pack(pady=5)
        # Download info:
        self.dl_info_title = ctk.CTkLabel(self.window, text="", font=("Helvetica", 16))
        self.dl_info_title.pack(pady=5)
        # Download bills:
        self.download_button = ctk.CTkButton(
            self.window,
            text="Download",
            command=self.start_download_thread)
        self.download_button.pack(pady=5)
        # Simple progress monitor:
        self.progress_label = ctk.CTkLabel(self.window, text=f"{prog} / {len(bill_numbers)} complete.", font=("Helvetica", 16))
        self.progress_label.pack(pady=5)
        
    def start_download_thread(self):
        thread = threading.Thread(target=self.download_bills)
        thread.start()

    # Select location to save files:
    def choose_save_location(self):
        selected_folder = filedialog.askdirectory(title="Select folder to save files")
        if selected_folder:
            self.save_location = selected_folder
            self.save_label.configure(text=f"Save location: {self.save_location}")
            self.download_button.configure(state="normal")
        else:
            self.save_label.configure(text="No folder selected")
            self.download_button.configure(state="disabled")

    # Set up Playwright to open browser headless and accept downloads automatically:
    def download_bills(self):
        global prog

        if not self.save_location:
            self.dl_info_title.configure(text="No folder selected. Please select a location.")
            return
        
        self.dl_info_title.configure(text="Starting download...")
        self.window.update_idletasks()

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, slow_mo=50)
            context = browser.new_context(accept_downloads=True)
            page = context.new_page()
            clear_screen()
            
            # For each of the bills specified in the .env file...:
            for bill in bill_numbers:
                filename = f"{bill}_{today_date}.xlsx"
                filepath = os.path.join(self.save_location, filename)
                self.dl_info_title.configure(text=f"Downloading {bill}")
                self.window.update_idletasks()

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

                prog += 1
                self.progress_label.configure(text=f"{prog} / {count} complete.")
                self.window.update_idletasks

            self.dl_info_title.configure(text="Download complete.")
            browser.close()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = BillsDownloaderApp(bill_numbers, url, today_date)
    app.run()