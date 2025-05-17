# 📰 Sky News Chile Headlines Extractor

## 📌 Overview
This Python script automatically fetches and extracts headlines and timestamps from [Sky News Chile](https://news.sky.com/topic/chile-6421). It scrapes news articles and neatly displays their **published dates** alongside their **headlines**, making it easier to scan for the latest news.

## 🔍 How It Works
1. **Dependency Check**  
   - The script first ensures that required libraries (`requests`, `beautifulsoup4`, and `lxml`) are installed.  
   - If any dependencies are missing, they are installed dynamically using `subprocess`.

2. **Web Scraping with `requests` and `BeautifulSoup`**  
   - The script sends an HTTP GET request to **Sky News Chile**.
   - The page's HTML is parsed using **BeautifulSoup**.

3. **Extracting News Headlines & Timestamps**  
   - The script searches for `<article>` elements, where news items are stored.
   - **Headline Extraction:** It grabs the headline from an `<a>` tag.
   - **Timestamp Extraction:** It retrieves the publication date from a `<time>` tag.

4. **Formatting & Displaying Results**  
   - Each headline is paired with its date (`YYYY-MM-DD`) for clear readability.
   - If a headline or timestamp is missing, a fallback message is displayed.