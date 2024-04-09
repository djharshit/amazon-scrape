
# Amazon India Product Scraper

This repository contains a Python script that automates the extraction of product details from Amazon India's search results. It is specifically designed to scrape data for 'bags' but can be easily modified for other products. The extracted details include the product name, URL, price, and rating, which are then saved into a CSV file for easy access and analysis.

## Features

- Scrapes product details from the first 10 pages of Amazon India's search results.
- Saves the product name, URL, price, and rating to a CSV file.
- Utilizes a fake User-Agent to mimic browser requests and bypass simple bot detection mechanisms.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- Installation of the `requests`, `bs4` (Beautiful Soup), and `faker` libraries.

You can install the necessary libraries using pip:

```bash
pip install requests beautifulsoup4 faker
```

## Usage

1. Clone the repository to your local machine.
2. Navigate to the script's directory.
3. Run the script using Python:

```bash
python amazon_scraper.py
```

4. Upon completion, check the `web\amazon\res.csv` file for the scraped data.

## Customization

To scrape data for products other than 'bags', modify the `query` dictionary's `'k'` value to your desired search term.

## Disclaimer

This script is for educational purposes only. Web scraping may be against the Terms of Service of some websites. Always check the website’s robots.txt file and terms before scraping. The structure of web pages can change over time, which may affect the script's functionality.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments

- This script was created for educational purposes and as a demonstration of basic web scraping techniques.