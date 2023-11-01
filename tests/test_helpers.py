import pytest
from jobtractor.helpers import filter_jobs, add_meta
from jobtractor.models import JobMeta

@pytest.fixture
def sample_links():
    return [
        {"text": "Data Scientist", "url": "https://example.com/job/1"},
        {"text": "Software Engineer", "url": "https://example.com/job/2"},
        {"text": "Data Analyst", "url": "https://example.com/job/3"},
        {"text": "Product Manager", "url": "https://example.com/job/4"},
    ]

def test_filter_jobs(sample_links):
    filtered_links = filter_jobs(sample_links)
    assert len(filtered_links) == 2
    assert all("data" in link["text"].lower() for link in filtered_links)

def test_add_meta():
    final_url = "https://example.com/job/1"
    html = "<html><body>Job details</body></html>"
    id_extract_re = r"/job/(\d+)"
    
    meta = add_meta(final_url, html, id_extract_re)
    assert isinstance(meta, JobMeta)
    assert meta.company_job_id == "1"
    assert meta.html == html
    assert meta.url == final_url
