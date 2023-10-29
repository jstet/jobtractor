from langchain.document_transformers import BeautifulSoupTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter


def process_for_llm(doc, chunk_size: int = 1000):
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=chunk_size, 
                                                                    chunk_overlap=0)
    splits = splitter.split_documents([doc])

    content = splits[0].page_content

    return content



