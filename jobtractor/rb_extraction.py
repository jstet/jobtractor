from bs4 import BeautifulSoup
from dagster import op


@op()
def extract_by_links(doc, rule, base_url: str=None):
    soup = BeautifulSoup(doc, "html.parser")
    links = soup.find_all("a", href=rule)
    links_dict = [{"url": (f"{base_url}{link.get('href')}" if base_url else link.get('href')), "text": link.text} for link in links]
    return links_dict


