"""TD Ameritrade Scrape"""
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.tdameritrade.com"


def search_td(query):
    """Search TD Ameritrade"""
    url = f"{BASE_URL}/search/results.page?q={query}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    return soup


def get_first_results_url(soup):
    """Get first result"""
    div = soup.findAll("div", {"class": ["module-container"]})[2]
    anchor = div.find("a")
    href = anchor.get("href")
    return href

def main():
    """Main"""
    soup = search_td("nvda")
    href = get_first_results_url(soup)
    print(href)


if __name__ == "__main__":
    main()
