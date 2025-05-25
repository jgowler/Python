# Movie Search Script

## Overview  
This Python script interacts with the OMDb API to retrieve and display movie details based on user input. It allows users to search for movies, view essential details such as the title, release date, genre, and plot, and continue searching until they decide to exit.

## Features
- Fetches movie data dynamically from the OMDb API.
- Ensures the API key is retrieved from environment variables.
- Loops for multiple searches until the user exits.
- Displays formatted movie details in the terminal.
- Implements error handling for HTTP failures and invalid API responses.

## How It Works

### 1. Setup and Dependencies  
- Installs missing packages (`httpx`, `python-dotenv`).
- Loads environment variables using `dotenv`.
- Retrieves the API key from the `.env` file.

### 2. User Input for Movie Search  
- Prompts the user to enter a movie title.
- Sends a request to the OMDb API using:  

http://www.omdbapi.com/?apikey={YOUR_API_KEY}&t={MovieName}


### 3. Handling API Response  
- If the movie is found, extracts:
- Title
- Release Date
- Genre
- Plot Summary
- If the movie is not found, prompts the user to enter another title.

### 4. Looping Until User Exits  
- After displaying the movie details, the script asks:  
`"Would you like to find another movie? (Yes/No)"`
- If the user enters `"Yes"`, the script continues searching.
- If the user enters `"No"`, the script exits.

## Example Output

Title: Rocky

Released: 03 Dec 1976

Genre: Drama, Sport

Plot: A small-time Philadelphia boxer gets a supremely rare chance to fight the world heavyweight champion in a bout in which he strives to go the distance for his self-respect.