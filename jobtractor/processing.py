from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from bs4 import BeautifulSoup
from dagster import op

@op()
def clean_html(html):
    soup = BeautifulSoup(html, "html.parser")
    forms = soup.find_all('form')
    for form in forms:
        form.decompose()
    text = soup.get_text().strip()
    return text

@op()
def process_for_llm(text, chunk_size: int = 1000):
    doc = Document(page_content=text, metadata={"source": "local"})
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=chunk_size, 
                                                                    chunk_overlap=0)
    splits = splitter.split_documents([doc])

    content = splits[0].page_content

    return content
