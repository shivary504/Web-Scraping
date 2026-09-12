# Web Scraping Projects

A collection of Python web scraping projects built using **Requests** and **BeautifulSoup**.

The repository currently contains two projects that demonstrate different approaches to extracting structured data from web pages.

## Projects

### 1. Daredevil Comics Scraper

Scrapes information about **Daredevil Vol. 1 (1964–1998)** from a locally saved HTML page from Marvel Database/Fandom.

**Data extracted:**

* Issue number
* Story title
* Release date
* Issue URL

**Tools used:**

* Python
* BeautifulSoup
* CSV

The scraper parses the saved HTML file and extracts the relevant elements using their HTML classes.

Output:

```text
daredevil/data/daredevil_comics.csv
```

---

### 2. Historical Currency Data Scraper

Scrapes historical currency exchange-rate data from X-Rates using HTTP requests.

The scraper generates a URL for each date in the selected period, sends an HTTP request, parses the returned HTML, and extracts the currency exchange rates.

**Data extracted:**

* Year
* Month
* Date
* Currency
* Exchange rate relative to 1 USD
* Inverse exchange rate

**Tools used:**

* Python
* Requests
* BeautifulSoup
* CSV

Output:

```text
currency/data/currency_rates.csv
```

## Technologies

```text
Python
Requests
BeautifulSoup
CSV
HTML Parsing
Web Scraping
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd web-scraping
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Requirements

```text
beautifulsoup4
requests
lxml
```

## Running the Scrapers

### Daredevil

```bash
python daredevil/scraper.py
```

### Currency

```bash
python currency/scraper.py
```

## What This Repository Demonstrates

These projects demonstrate two common web-scraping workflows:

1. **Parsing an existing HTML document**

   * Load a local HTML file
   * Parse it with BeautifulSoup
   * Locate relevant HTML elements
   * Extract and clean the data
   * Save the results as CSV

2. **Requesting and parsing web pages**

   * Generate URLs dynamically
   * Send HTTP requests using Requests
   * Parse the returned HTML
   * Extract structured information
   * Store the results in CSV format

## Disclaimer

The scraped data belongs to its respective source websites. This repository is intended for educational and portfolio purposes.
