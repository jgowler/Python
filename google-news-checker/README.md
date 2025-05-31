# Sky News Chile Headlines Extractor  

## Overview  
This Python script automatically fetches and extracts **headlines and timestamps** from [Sky News Chile](https://news.sky.com/topic/chile-6421).  
It scrapes news articles and organizes them by **published date**, enabling quick and efficient news scanning.

## How It Works  

### 1. Dependency Check  
- Ensures required libraries (`requests`, `beautifulsoup4`, and `lxml`) are installed.  
- Dynamically installs missing dependencies using `subprocess`.  

### 2. Web Scraping with `requests` and `BeautifulSoup`  
- Sends an HTTP GET request to **Sky News Chile**.  
- Parses the page's HTML using **BeautifulSoup** for structured data extraction.  

### 3. Extracting News Headlines & Timestamps  
- Identifies `<article>` elements containing news stories.  
- **Headline Extraction:** Retrieves news titles from `<a>` tags.  
- **Timestamp Extraction:** Extracts publication dates from `<time>` tags.  

### 4. Formatting & Displaying Results  
- Outputs headlines paired with their **publication date (`YYYY-MM-DD`)** for readability.  
- Displays fallback messages if a headline or timestamp is missing.  