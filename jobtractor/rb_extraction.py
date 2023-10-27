from bs4 import BeautifulSoup


def extract_links(doc, rule):
    soup = BeautifulSoup(doc, "html.parser")

    links = soup.find_all("a", href=rule)
    links = [link.get("href") for link in links]
    return links

