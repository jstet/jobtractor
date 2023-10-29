from jobtractor.rb_extraction import extract_links
from jobtractor.llm_extraction import extract
from jobtractor.loader import load
from jobtractor.processing import process_for_llm
from jobtractor.console import console
import re
from bs4 import BeautifulSoup
from datetime import datetime
from langchain.docstore.document import Document

def filter_jobs(links):
    return [link for link in links if "data" in link["text"].lower()]

def add_meta(job, url, html, company_job_id):
    """
    Adds metadata to the job object.

    Args:
        job (dict): The job object to add metadata to.
        url (str): The URL of the job.
        html (str): The HTML content of the job.
        company_job_id (str): The ID of the job in the company database.

    Returns:
        dict: The job object with added metadata.
    """
    job["company_job_id"] = company_job_id
    job["html"] = html
    job["url"] = url
    job["extracted_at"] = datetime.now()
    return job


def greenhouse(html, company):
    """
    Extract job information from the given HTML page for a specific company if that comapny uses greenhouse.
    
    Args:
        html (str): The HTML content of the page.
        company (str): The name of the company.
    
    Returns:
        list: A list of job objects containing the extracted information.
    """
    jobs = []
    links = extract_links(html, rule=lambda href: href and "https://grnh.se" in href)
    links = filter_jobs(links)
    for link in links:
        url = link["url"]
        console.log(f"Trying: {url}")
        try:
            html, final_url = load(url, avoid_url=f"https://boards.greenhouse.io/{company}")
        except ValueError as e:
            console.log(f"Error: {e}. Job is probably no longer open")
            continue
        soup = BeautifulSoup(html, "html.parser")
        forms = soup.find_all('form')
        for form in forms:
            form.decompose()
        text = soup.get_text()
        doc =  Document(page_content=text, metadata={"source": "local"})
        content = process_for_llm(doc, chunk_size=300)
        job = extract(content, url=url, single=True)  
        company_job_id = re.search(r"/(\d+)\?", final_url).group(1)
        job = add_meta(job, final_url, html, company_job_id)  
        jobs.append(job)
    return jobs