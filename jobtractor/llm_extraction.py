from jobtractor.models import Job
from langchain.chat_models import ChatLiteLLM
from dagster import op
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)
from dotenv import load_dotenv

load_dotenv()

llm = ChatLiteLLM(model="perplexity/mistral-7b-instruct", temperature=0.0)

@op()
def text_extract_single(content: str):

    parser = PydanticOutputParser(pydantic_object=Job)

    prompt = ChatPromptTemplate(
        messages=[
            HumanMessagePromptTemplate.from_template(
                "Please answer the following query as specified and do not add additional information. \n\n{format_instructions}\n\n{query}\n"
            )
        ],
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    _input = prompt.format_prompt(query=content)
    output = llm(_input.to_messages())
    output_content = output.content.replace("\\_", "_").replace("}}","}")
    summary_start = output_content.find('"summary"')
    if summary_start != -1:
        output_content = output_content[:summary_start-2] + "}" 
    parsed = parser.parse(output_content)
    return parsed
