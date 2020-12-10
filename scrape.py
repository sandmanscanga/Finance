"""TD Ameritrade Scrape"""
import requests
from bs4 import BeautifulSoup

STOCK = "nvda"


def search_td(query):
    """Search TD Ameritrade"""
    base_url = "https://www.tdameritrade.com"
    url = f"{base_url}/search/results.page?q={query}"
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


def get_fund_data(symbol):
    """Get fundamental data from extracted symbol"""
    res_url = "https://research.tdameritrade.com"
    fund_url = f"{res_url}/grid/public/research/stocks/fundamentals"
    resp = requests.get(fund_url, params={"symbol": symbol})
    return BeautifulSoup(resp.text, "lxml")


def extract_fund_hrefs(soup):
    """Extracts hrefs from fundamental data"""
    div = soup.find("div", {"class": ["stock-fundamentals-page"]})
    nav = div.find("nav").find("nav")

    hrefs = []
    for anchor in nav.findAll("a"):
        href = anchor.get("href")
        hrefs.append(href)

    return hrefs


def main():
    """Main"""
    soup = search_td(STOCK)
    results_url = get_first_results_url(soup)
    symbol = extract_symbol(results_url)
    soup = get_fund_data(symbol)
    hrefs = extract_fund_hrefs(soup)
    print(hrefs)


if __name__ == "__main__":
    main()
