import argparse
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import ChatPromptTemplate

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

def main(query_text):
    embedding_function = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the database
    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    if len(results) == 0 or results[0][1] < 0.7:
        return "No relevant results found.", []

    # Extract context and format the query
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    # Use ChatOpenAI to get a response
    model = ChatOpenAI()
    response = model.invoke(prompt)

    # Extract response content
    response_content = response.content if hasattr(response, 'content') else response

    # Extract sources
    sources = []
    for doc, _score in results:
        source = doc.metadata.get("source", "Unknown").replace("data\\", "").replace("data/", "")
        page = doc.metadata.get("page_number", "Unknown")
        sources.append(f"{source}, Page: {page}")

    return response_content, sources