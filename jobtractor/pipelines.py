from jobtractor.loader import load
from jobtractor.rb_extraction import extract_links
from jobtractor.llm_extraction import extract
from jobtractor.processing import process_for_llm
from jobtractor.console import console
from bs4 import BeautifulSoup
from langchain.docstore.document import Document


def run(url):
    url = "https://www.blueorchard.com/careers/"
    docs = load(url)
    content = process_for_llm(docs)
    data = extract(content)
    print(data)


def greenhouse(html, company):
    jobs = []
    links = extract_links(html, rule=lambda href: href and "https://grnh.se" in href)
    for url in links:
        console.log(f"Trying: {url}")
        try:
            html = load(url, avoid_url=f"https://boards.greenhouse.io/{company}")
        except ValueError as e:
            console.log(f"Error: {e}. Job is probably no longer open")
            continue
        soup = BeautifulSoup(html, "html.parser")
        # search in soup for text "The job you are looking for is no longer open."
        # if soup.find(text="The job you are looking for is no longer open.") is not None:
        soup = soup.find('div', {'id': 'app_body'})  
        forms = soup.find_all('form')
        for form in forms:
            form.decompose()
        doc =  Document(page_content=soup.get_text(), metadata={"source": "local"})
        content = process_for_llm(doc)
        job = extract(content, url=url, single=True)    
        job["url"] = url
        jobs.append(job)
    return jobs



def wikimedia():
    url = "https://wikimediafoundation.org/about/jobs/"
    html = load(url)
    jobs = greenhouse(html, "wikimedia")
    return jobs
    

        


