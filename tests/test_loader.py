from jobtractor.loader import load
from langchain.schema import Document

def test_load():
    doc = load("https://wikimediafoundation.org/about/jobs")
    assert isinstance(doc, Document)
    text = doc.page_content
    assert len(text) > 0
    assert isinstance(text, str)
    # save to file
    with open("tests/fixtures/wikimedia_10_23.txt", "w") as f:
        f.write(text)

