from langchain.chat_models import ChatLiteLLM
from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)
from typing import Sequence

from dotenv import load_dotenv

load_dotenv()

class Job(BaseModel):
    job_name: str
    job_location: str

class Jobs(BaseModel):
    """Identifying information about all jobs in a text."""
    jobs: Sequence[Job]

llm = ChatLiteLLM(model="perplexity/mistral-7b-instruct", temperature=0.0)

def extract(content: str, url,single: bool = True):

    if single:
        parser = PydanticOutputParser(pydantic_object=Job)
    else:
        parser = PydanticOutputParser(pydantic_object=Jobs)

    prompt = ChatPromptTemplate(
        messages=[
            HumanMessagePromptTemplate.from_template(
                "Answer the user query. \n {format_instructions} \n {query} \n"
            )
        ],
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    _input = prompt.format_prompt(query=content)
    output = llm(_input.to_messages())
    output_content = output.content.replace("\\_", "_").replace("}}","}")
    parsed = parser.parse(output_content)
    return parsed.model_dump()
