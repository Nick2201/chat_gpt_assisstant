import json


class DbBase:

    def __init__(self, ConfigPath: str):
        self._config = None
        self._config_path = ConfigPath
        self.dialect = 'postgresql'

    @property
    def connect_url(self):
        with open(self._config_path, 'r') as file:
            self._config = json.load(file)
            return self.dialect + '://{user}:{password}@{host}:{port}/{database}'.format(**self._config)

    @property
    def config(self):
        return self._config

    @property
    def path(self):
        return self._config_path


from sqlalchemy.orm import mapper, relationship, sessionmaker

from sqlalchemy import (
    MetaData, Table, Column, Integer, String, create_engine, DateTime, select
)

engine = create_engine(DbBase(r'C:\Users\nickl\My_softwares\Own_Packacges\chatgpt_assistant\docs\db_connect.json').connect_url, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()
chat_gpt_data = Table(
    'chat_gpt_response', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('topic', String),
    Column('user', String),
    Column('assistant', String),
    Column("user_input", String),
    Column("chat_response", String),
    Column("time_add", DateTime))
metadata.create_all(engine)
# distinct_names = select([chat_gpt_data.user.distinct()]).execute().fetchall()

# from sqlalchemy.orm import sessionmaker
# from datetime import datetime
#
# def save_chat_data(topic, user, assistant, user_input, chat_response):
# Session = sessionmaker(bind=engine)
# session = Session()
#
# new_data = chat_gpt_data.\
#     insert().\
#     values(
#         topic=topic,
#         user=user,
#         assistant=assistant,
#         user_input=user_input,
#         chat_response=chat_response,
#         time_add=datetime.now()
#         )
#
# session.execute(new_data)
# session.commit()
# session.close()
# [item.user for item in session.query(chat_gpt_data).distinct("user")]

