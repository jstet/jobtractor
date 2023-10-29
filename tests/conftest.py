import pytest
from langchain.docstore.document import Document

@pytest.fixture
def orchard():
    with open('tests/fixtures/blue_orchard_10_23.txt', 'r') as f:
        data = f.read()
    return data


@pytest.fixture
def noodle():
    with open('tests/fixtures/noodle_ai_10_23.txt', 'r') as f:
        data = f.read()
    return data

@pytest.fixture
def wikimedia():
    with open('tests/fixtures/wikimedia_10_23.txt', 'r') as f:
        data = f.read()
    return data