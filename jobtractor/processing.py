from langchain.document_transformers import BeautifulSoupTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter


def process_for_llm(doc):
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=1000, 
                                                                    chunk_overlap=0)
    splits = splitter.split_documents([doc])

    content = splits[0].page_content

    return content



