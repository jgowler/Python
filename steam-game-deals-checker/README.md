# Steam Game Deals Visualization Script

## Overview
This script retrieves game deals from the CheapShark API and visualizes the savings on discounted Steam games. It fetches games on sale under $15 and displays the top 15 deals using a distribution plot.

## Features
- Automatically installs required dependencies
- Fetches the latest Steam game deals via CheapShark API
- Converts JSON data into a Pandas DataFrame
- Sorts and selects the top 15 deals by savings
- Generates a **Seaborn** graph to visualize savings percentages