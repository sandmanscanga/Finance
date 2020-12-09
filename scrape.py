"""TD Ameritrade Scrape"""
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.tdameritrade.com"

# https://www.tdameritrade.com/search/results.page?q=nvda


def search_td(query):
    """Search TD Ameritrade"""
    url = f"{BASE_URL}/search/results.page?q={query}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    return soup


def main():
    """Main"""
    soup = search_td("nvda")
    print(soup.prettify())


if __name__ == "__main__":
    main()
