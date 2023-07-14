import streamlit as st
from streamlit_chat import message

from database import get_redis_connection
from chatbot import RetrievalAssistant, Message

# Initialise database

## Initialise Redis connection
redis_client = get_redis_connection()

# Set instruction

# System prompt requiring Question and Year to be extracted from the user
system_prompt = '''
You are a helpful sports knowledge base assistant. You need to capture a Question and Year from each customer.
The Question is their query on sport rule, and the Sport is the sport of concern, which is either basketball or soccer.
Think about this step by step:
- The user will ask a Question
- You will ask them for the Sport if their question didn't include a Sport
- Once you have the Sport, say "searching for answers".

Example:

User: I'd like to know how many players on each team

Assistant: Certainly, what sport would you like this for?

User: basketball please.

Assistant: Searching for answers.
'''

### CHATBOT APP

st.set_page_config(
    page_title="Streamlit Chat - Demo",
    page_icon=":robot:"
)

st.title('Sport Rule Chatbot')
st.subheader("Ask me about sport rules")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def query(question):
    response = st.session_state['chat'].ask_assistant(question)
    return response

prompt = st.text_input(f"What do you want to know: ", key="input")

if st.button('Submit', key='generationSubmit'):

    # Initialization
    if 'chat' not in st.session_state:
        st.session_state['chat'] = RetrievalAssistant()
        messages = []
        system_message = Message('system',system_prompt)
        messages.append(system_message.message())
    else:
        messages = []


    user_message = Message('user',prompt)
    messages.append(user_message.message())

    response = query(messages)

    # Debugging step to print the whole response
    #st.write(response)

    st.session_state.past.append(prompt)
    st.session_state.generated.append(response['content'])

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
