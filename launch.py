import openai
import streamlit as st
from streamlit_chat import message
from dataclasses import dataclass, field
from typing import List
from datetime import datetime
from app.model.participants import MainComponent, UserConfig, AssistantConfig, TopicConfig
from app.model.db_models import engine, Session, chat_gpt_data
from sqlalchemy import distinct
import os
from app.config import CONFIG

# from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationEntityMemory
# from langchain.chains.conversation.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
# from langchain.llms import OpenAI
'''
How I can for chatGot api remember aswers and question and write asnwers with old informations (asnwers ans question before)
'''
# openai.api_key = os.getenv("OPENAI_API_KEY")

# response = False
session = Session()
class CustomChatGPT:
    def __init__(self):
        self.api_key = None
        self.message_history = []
        self.tokens_have = 4097  # TODO: make more flexability
        self.session = Session()

        self.main_topic = None
        self.parameters = {
            "prompt_tokens": "",
            "completion_tokes": "",
            "total_tokens_used": "",
            "cost_of_response": "",
            'left to go over': '',
        }

    def take_topic(self, topic: TopicConfig):
        self.message_history = topic.message_history
        self.main_topic = topic

    def connect_to_lm(self):
        list_api = open(CONFIG['API_KEYS'], "r").read().strip(
            "\n").split("\n")
        self.api_key = list_api[1]
        openai.api_key = self.api_key

    def ask_chat(self, user_input):
        self.message_history.append({"role": "user", "content": user_input})

        chat_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.message_history,
            temperature=1)
        print(self.message_history)
        chat_message = chat_response["choices"][0]["message"]["content"]

        # prompt_tokens = chat_response["usage"]["prompt_tokens"]
        self.parameters["prompt_tokens"] = chat_response["usage"]["prompt_tokens"]
        self.parameters['completion_tokes'] = chat_response["usage"]["completion_tokens"]
        self.parameters['total_tokens_used'] = chat_response["usage"]["total_tokens"]
        self.parameters['left to go over'] = int(self.tokens_have) - int(self.parameters['total_tokens_used'])

        self.message_history.append({"role": "assistant", "content": chat_message})

        new_data = chat_gpt_data. \
            insert(). \
            values(
            topic=self.main_topic.name,
            user=self.main_topic._default_user.name,
            assistant=self.main_topic._default_assistant.name,
            user_input=user_input,
            chat_response=chat_message,
            time_add=datetime.now()
        )
        self.session.execute(new_data)
        self.session.commit()
        return chat_message

# storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if "input" not in st.session_state:
    st.session_state["input"] = ""
if "stored_session" not in st.session_state:
    st.session_state["stored_session"] = []

senior_python = AssistantConfig(
    name="senior_python",
    _description='Senior Python developer',
)
# junior_developer = UserConfig(
#     name="senior_python",
#     _description='Senior Python developer',
# )
print(senior_python.pre_text)
ifrs = TopicConfig(
    name="ifrs",
    _description='About FRS',
)
print(senior_python.pre_text)

chat = CustomChatGPT()
chat.connect_to_lm()
chat.take_topic(ifrs)

st.title("ChatGPT Web App")

# Create a text input


# Create a button to clear the text input
col1, col2 = st.columns([3,1])
with st.sidebar:
    st.title("Usage Stats:")
    st.markdown("""---""")
    st.write(f"Promt tokens used : ", chat.parameters['prompt_tokens'])
    st.write("Completion tokens used :", chat.parameters['completion_tokes'])
    st.write("Total tokens used :", chat.parameters['total_tokens_used'])
    st.write("For next step You have: ", chat.parameters['left to go over'])
    st.markdown("""---""")


    option_user = st.selectbox(
        'Whats User You want',
        [item.user for item in session.query(chat_gpt_data).distinct("user")])
    option_assistant = st.selectbox(
        'Whats Assistant You wanna have',
        [item.assistant for item in session.query(chat_gpt_data).distinct("assistant")])
    option_topic = st.selectbox(
        'Whats THe Topic??',
        [item.topic for item in session.query(chat_gpt_data).distinct("topic")])
    # session = Session()
with col1:
    user_input = st.text_area("You:", key='input', max_chars=10000, value='')
    if st.button("go"):

        output = chat.ask_chat(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)

        st.header("Streamlit + OpenAI ChatGPT API")

        st.markdown("""---""")
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated']) - 1, -1, -1):
            message(st.session_state["generated"][i], key=str(i), avatar_style="initials", seed=senior_python.name)
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user', avatar_style="initials", seed='ND')

with col2:
    st.header("History")
    st.markdown("""---""")
    st.write(chat.message_history)




