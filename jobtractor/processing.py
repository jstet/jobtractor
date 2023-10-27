from langchain.document_transformers import BeautifulSoupTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter


def process(doc):
    bs_transformer = BeautifulSoupTransformer()
    docs_transformed = bs_transformer.transform_documents([doc],tags_to_extract=["p"])

    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=1000, 
                                                                    chunk_overlap=0)
    splits = splitter.split_documents(docs_transformed)

    content = splits[0].page_content
    
    return content