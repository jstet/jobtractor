from langchain.chat_models import ChatLiteLLM
from pydantic import BaseModel, Field, validator
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from typing import Sequence, Optional
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import os, litellm

from dotenv import load_dotenv

load_dotenv()


class Job(BaseModel):
    job_name: str
    job_location: str


class Jobs(BaseModel):
    """Identifying information about all jobs in a text."""

    people: Sequence[Job]


llm = ChatLiteLLM(model="perplexity/mistral-7b-instruct", temperature=0.0)

# codellama-34b-instruct	completion(model="perplexity/codellama-34b-instruct", messages)
# llama-2-13b-chat	completion(model="perplexity/llama-2-13b-chat", messages)
# llama-2-70b-chat	completion(model="perplexity/llama-2-70b-chat", messages)
# mistral-7b-instruct	completion(model="perplexity/mistral-7b-instruct", messages)
# replit-code-v1.5-3b	completion(model="perplexity/replit-code-v1.5-3b", messages)



def extract(content: str, single: bool = True):

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
    print(output)
    output_content = output.content.replace("\\_", "_")
    return parser.parse(output_content)
