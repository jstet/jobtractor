from langchain.document_loaders import AsyncHtmlLoader

def load(url):
    urls = [url]
    loader = AsyncHtmlLoader(urls)
    docs = loader.load()
    return docs[0]