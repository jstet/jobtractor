from jobtractor.loader import load
from langchain.schema import Document

def test_load():
    docs = load("https://www.blueorchard.com/careers/")
    assert isinstance(docs, list)
    assert len(docs) > 0
    assert isinstance(docs[0], Document)
    text = docs[0].page_content
    assert len(text) > 0
    assert isinstance(text, str)

