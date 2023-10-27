from jobtractor.loader import load
from jobtractor.extraction import extract
from jobtractor.processing import process


def run(url):
    url = "https://www.blueorchard.com/careers/"
    docs = load(url)
    content = process(docs)
    data = extract(content)
    print(data)