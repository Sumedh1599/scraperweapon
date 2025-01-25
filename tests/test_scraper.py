import sys
import os

# Add the scraperweapon directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraperweapon.scraper import Scraper

def test_scraper():
    """
    Test the Scraper class with a LinkedIn job search.
    """
    scraper = Scraper(use_proxies=False, use_headless=True)
    url = "https://www.linkedin.com/jobs/search/?keywords=Data+Scientist&location=London"
    content = scraper.get(url)

    if content:
        print("Successfully fetched page content.")
    else:
        print("Failed to fetch page content.")

if __name__ == "__main__":
    test_scraper()
