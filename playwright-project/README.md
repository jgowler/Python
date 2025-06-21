# Playwright-Based Data Retrieval Tool

This app was created at request to make the process of checking certain bills published publically without needing to manually go through each step. As there is no public API to access this information a workaround in the form of Playwright is used to go through each step what would be required to be done manually done programmatically.

**Setup and Dependencies**  

- Once the virtual environment has been set up and activated run "**PLAYWRIGHT_BROWSERS_PATH=0 playwright install <BROWSER>**" (in this case <BROWSER> is "chromium" although this can be whatever option you prefer).
This is required as the browser files will need to be included, otherwise the app will not detect the required files once compiled as they will not be included.
- All packages used during the development of this program can be found in the **"requirements.txt"** file although these are the ones present within the development venv.

**How the app works**

- The list of bills are included within a list in the app itself. For this app there is currently no way to test this as it was made to spec and did not require altering.
- Once a save location has been selected the Download button will then begin to work, it is disabled until a location is selected.
- The app will use playwright to do each step required to get the specified bills and download them to the chosen location.
- The progress of the run will be shown as it progresses. The current bill being downloaded will be displayed within the window.
- After the run is complete there will be on screen confirmation.

**Personal goals during development**

- This project allowed me to get more hands on experience using **Virtual Environments** which was useful in ensuring the required dependencies for the project could be listed for those who download the code in the **requirements.txt** file.
- I also got experience using **pyinstaller** and **Inneo Setup Compiler** to package the .py app into a single file, then to a basic setup wizard to be installed on another system that does not have Python installed.
- This project pushed me to work on all parts of getting a piece of software developed; from planning and design through to testing the app from the terminal and removing redundant code, to compiling and running on another system.