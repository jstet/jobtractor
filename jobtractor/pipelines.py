from jobtractor.loader import load
from jobtractor.rb_extraction import extract_links
from jobtractor.llm_extraction import extract
from jobtractor.processing import process_for_llm
from bs4 import BeautifulSoup
from langchain.docstore.document import Document


def run(url):
    url = "https://www.blueorchard.com/careers/"
    docs = load(url)
    content = process_for_llm(docs)
    data = extract(content)
    print(data)


def wikimedia():
    url = "https://wikimediafoundation.org/about/jobs/"
    html = load(url,to_str=True)
    links = extract_links(html, rule=lambda href: href and "https://grnh.se" in href)
    jobs = []
    for link in links:
        html = load(link, to_str=True)
        soup = BeautifulSoup(html, "html.parser")
        soup = soup.find('div', {'id': 'app_body'})
        # remove application form
        forms = soup.find_all('form')
        for form in forms:
            form.decompose()
        doc =  Document(page_content=soup.get_text(), metadata={"source": "local"})
        content = process_for_llm(doc)
        job = extract(content, single=True)
        print(job)
        jobs.append(job)
    print(jobs)
    

        


