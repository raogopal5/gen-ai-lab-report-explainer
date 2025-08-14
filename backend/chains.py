from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from config import MODEL_NAME, TEMPERATURE, MAX_TOKENS


def get_explainer_chain():
    llm = Ollama(model=MODEL_NAME, temperature=TEMPERATURE, num_predict=MAX_TOKENS)
    prompt_template = """
You are a helpful and compassionate medical assistant.

A patient has provided the following lab report:

{report_text}

Please explain the lab results in simple, non-technical language.
Mention any values that seem outside typical ranges in general terms.
Suggest what the patient should discuss with their doctor.
Include the disclaimer: "This is not medical advice. Please consult your doctor."
"""
    prompt = PromptTemplate(input_variables=["report_text"], template=prompt_template)
    return LLMChain(llm=llm, prompt=prompt)
