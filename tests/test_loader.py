from jobtractor.loader import load
from langchain.schema import Document

def test_load():
    doc, final_url = load("https://wikimediafoundation.org/about/jobs")
    assert len(doc) > 0
    assert isinstance(doc, str)
    # save to file
    with open("tests/fixtures/wikimedia_10_23.txt", "w") as f:
        f.write(doc)

