import pytest
from langchain.docstore.document import Document

@pytest.fixture
def orchard_loaded():
    with open('tests/fixtures/orchard_loaded.txt', 'r') as f:
        data = f.read()
    doc =  Document(page_content=data, metadata={"source": "local"})
    return doc