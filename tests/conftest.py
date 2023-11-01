import pytest
import json

@pytest.fixture
def orchard_html():
    with open('tests/fixtures/html/blue_orchard_10_23.txt', 'r') as f:
        data = f.read()
    return data


@pytest.fixture
def noodle_html():
    with open('tests/fixtures/html/noodle_ai_10_23.txt', 'r') as f:
        data = f.read()
    return data

@pytest.fixture
def wikimedia_html():
    with open('tests/fixtures/html/wikimedia_10_23.txt', 'r') as f:
        data = f.read()
    return data

@pytest.fixture
def climeworks_html():
    with open('tests/fixtures/html/climeworks_10_29.txt', 'r') as f:
        data = f.read()
    return data

@pytest.fixture
def wikimedia_organization():
    file_path = 'tests/fixtures/organizations/wikimedia.json'
    with open(file_path) as file:
        data = json.load(file)
    return data