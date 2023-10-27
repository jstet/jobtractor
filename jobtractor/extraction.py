from langchain.chains import create_extraction_chain
from langchain.chat_models import ChatLiteLLM
from langchain.llms.utils import enforce_stop_tokens
from typing import List, Optional, Any
from functools import partial
import os, litellm

from dotenv import load_dotenv

load_dotenv()

# IMPORTANT - Set this to TRUE to add the function to the prompt for Non OpenAI LLMs
litellm.add_function_to_prompt = True # set add_function_to_prompt for Non OpenAI LLMs


def _call(
    self,
    prompt: str,
    stop: Optional[List[str]] = None,
    run_manager: Optional[Any] = None,
    **kwargs: Any,
) -> str:
    text_callback = None
    if run_manager:
        text_callback = partial(run_manager.on_llm_new_token, verbose=self.verbose)
    text = ""
    params = {**self._default_params(), **kwargs}
    for token in self.client.generate(prompt, **params):
        if text_callback:
            text_callback(token)
        text += token
    if stop is not None:
        text = enforce_stop_tokens(text, stop)
    
    # Remove control characters
    text = text.translate(str.maketrans('', '', ''.join(map(chr, range(32)))))
    
    return text


llm = ChatLiteLLM(model="perplexity/mistral-7b-instruct")


llm._call_ = _call

schema = {
    "properties": {
        "job_title": {"type": "string"},
        "job_link": {"type": "string"},
    },
    "required": ["job_title", "job_link"],
}

def extract(content: str):
    return create_extraction_chain(schema, llm=llm).run(content)

