from langchain.document_loaders import AsyncChromiumLoader

def load(url,to_str:bool=False):
    urls = [url]
    loader = AsyncChromiumLoader(urls)
    html = loader.load()
    if to_str:
        return str(html[0].page_content)
    return html[0]