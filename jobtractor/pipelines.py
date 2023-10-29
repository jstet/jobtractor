from jobtractor.loader import load
from jobtractor.rb_extraction import extract_links
from jobtractor.llm_extraction import extract
from jobtractor.processing import process_for_llm
from jobtractor.console import console
import re
from bs4 import BeautifulSoup
from datetime import datetime
from langchain.docstore.document import Document


def run(url):
    url = "https://www.blueorchard.com/careers/"
    docs = load(url)
    content = process_for_llm(docs)
    data = extract(content)
    print(data)

def add_meta(job, url, html, company_job_id):
    job["company_job_id"] = company_job_id
    job["html"] = html
    job["url"] = url
    job["extracted_at"] = datetime.now()
    return job


def greenhouse(html, company):
    jobs = []
    links = extract_links(html, rule=lambda href: href and "https://grnh.se" in href)
    for url in links:
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



def wikimedia():
    url = "https://wikimediafoundation.org/about/jobs/"
    html, final_url = load(url)
    jobs = greenhouse(html, "wikimedia")
    return jobs
    

        


