import pytest
from langchain.docstore.document import Document

@pytest.fixture
def orchard_doc():
    with open('tests/fixtures/blue_orchard_10_23.txt', 'r') as f:
        data = f.read()
    doc =  Document(page_content=data, metadata={"source": "local"})
    return doc

@pytest.fixture
def orchard_str():
    with open('tests/fixtures/blue_orchard_10_23.txt', 'r') as f:
        data = f.read()
    return data


@pytest.fixture
def noodle_str():
    with open('tests/fixtures/noodle_ai_10_23.txt', 'r') as f:
        data = f.read()
    return data

@pytest.fixture
def wikimedia_str():
    with open('tests/fixtures/wikimedia_10_23.txt', 'r') as f:
        data = f.read()
    return data