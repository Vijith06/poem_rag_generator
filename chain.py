from model import create_chat_groq
import prompt 


def generate_poem(topic):
    '''
    function to  generate_poem
     
    Args:
        topic(str): Topic of the poem

    Returns : 
        response.content(str)
    '''
    prompt_template=prompt.poem_generator_prompt_from_hub()
    llm=create_chat_groq()

    chain = prompt_template | llm

    response = chain.invoke({
        "topic" : topic
    })
    return response.content

# def generate_quiz(level,field):
#     '''
#     function to  generate quiz
     
#     Args:
#         level(str)= Level of the quiz
#         fiels(str)=At which subject(like maths,science and etc..)

#     Returns : 
#           response.content(str)

#     '''
    
#     prompt_template=prompt.quiz_generator_prompt_from_hub()
#     llm=create_chat_groq()

#     chain = prompt_template | llm

#     response = chain.invoke({
#         "level" : level,
#         "field": field
#     })
    
#     return response.content