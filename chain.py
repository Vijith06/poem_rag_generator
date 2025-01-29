from langchain_core.output_parsers import StrOutputParser
import model
import prompt
import vectordb


#### GENERATION ####
def generate_poem_chain(topic):
    """
    Generate Poem using basic prompt LLM chain

    Args:
        topic - topic for the poem

    Returns:
        response.content -> str
    """
        
    llm = model.create_chat_groq_model()

    prompt_template = prompt.poem_generator_prompt()
    # prompt_template = prompts.poem_generator_prompt_from_hub()

    chain = prompt_template | llm

    response = chain.invoke({
        "topic" : topic
    })
    return response.content


#### RETRIEVAL and GENERATION ####

def generate_poem_rag_chain(topic, vector):
    """
    Creates a RAG chain for retrieval and generation.

    Args:
        topic - topic for retrieval
        vectorstore ->  Instance of vector store 

    Returns:
        rag_chain -> rag chain
    """
    # Prompt
    prompt_template = prompt.poem_generator_rag_prompt()

    # LLM
    llm = model.create_chat_groq_model()

    # Post-processing
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    retriever = vectordb.retrieve_from_chroma(topic, vectorstore=vector)
    # Chain
    rag_chain = prompt_template| llm | StrOutputParser()

    response = rag_chain.invoke({
        "context" : format_docs(retriever),
        "topic": topic
    })    

    return response
