from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

PROMPT_TEMPLATE = """
Answer the question:

---
Restrictions:
response in portugues BR

{question}
"""

def query_model(query_text: str) -> str:
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(question=query_text)

    model = Ollama(model="llama3")
    response_text = model.invoke(prompt)

    return response_text
