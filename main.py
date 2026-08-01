from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

from retriver import retriever


def chatbot(question):
    prompt = PromptTemplate.from_template(
        """
    you are an expert document analyzer. use the content of the document given below and answer the questions
    document : {document}
    Question: {question}

    """
    )

    chat = ChatOllama(model="llama3")
    chain = prompt | chat

    
    docs = retriever.invoke(question)
    docum = "\n\n".join(
        doc.page_content for doc in docs
        )
    response = chain.invoke(
            {
                "document":docum,
                "question":question
            }
        )
    return response.content


