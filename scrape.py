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
    url = anchor.get("href")
    return url


def extract_symbol(url):
    """Extract symbol from url"""
    return url.split("&")[-1].split("=")[-1]


def get_fundamental_data(symbol):
    """Get fundamental data from extracted symbol"""
    res_url = "https://research.tdameritrade.com"
    fund_url = f"{res_url}/public/stocks/overview/overview.asp"
    params = {
        "fromPage": "overview",
        "display": "",
        "fromSearch": "true",
        "symbol": symbol
    }
    resp = requests.get(fund_url, params=params)
    html = resp.text
    soup = BeautifulSoup(html, "lxml")
    return soup

def extract_fund_href(soup):
    div = soup.find("div", {"class": ["stock-fundamentals-page"]})
    print(div.prettify())


def main():
    """Main"""
    soup = search_td("nvda")
    results_url = get_first_results_url(soup)
    symbol = extract_symbol(results_url)
    soup = get_fundamental_data(symbol)
    extract_fund_href(soup)


if __name__ == "__main__":
    main()
