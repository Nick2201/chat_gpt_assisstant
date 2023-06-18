from dataclasses import dataclass
import openai
from dataclasses import dataclass, field
from typing import List, Dict
from datetime import datetime


# def context_creator():
#     return

@dataclass
class MainComponent:
    name: str
    _description: str

    logs_item: str
    pre_text: Dict[str, str] = field(init=False, repr=False)

    def __post_init__(self):
        self.pre_text = {"role": self.logs_item,'content': self._description}


@dataclass
class UserConfig(MainComponent):
    logs_item: str = 'user'


@dataclass
class AssistantConfig(MainComponent):
    logs_item: str = 'system'


@dataclass
class TopicConfig(MainComponent):
    # current message history
    _default_user: UserConfig = UserConfig(
        name="nick",
        _description='Junior Python developer',
    )
    _default_assistant: AssistantConfig = AssistantConfig(
        name="senior_python",
        _description='You are Senior Python developer and every your need write two blocks write block "['
                     'explanation]" and below write "explanation" write block "[example]" and below right code with '
                     'use Software Design Principles.',
    )

    logs_item: str = 'system'
    message_history: List = field(init=False, repr=False)


    def __post_init__(self):
        self.message_history = [self._default_assistant.pre_text,self._default_user.pre_text]


# nick_developer = UserConfig(
#     name="nick",
#     _description='Junior Python developer')
#
# print(nick_developer.pre_text)
#
# senior_python = AssistantConfig(
#     name="senior_python",
#     _description='Senior Python developer',
# )
# print(senior_python.pre_text)
# ifrs = TopicConfig(
#     name="ifrs",
#     _description='About FRS'
# )
# print(senior_python.pre_text)
# print(ifrs.message_history)

#
# class AssistantBase:  # aggregates
#     def __init__(self, assistant_base_name):
#         self.name_base = assistant_base_name
#         self.assistant_list_base = []
#
#     def add_new_assistant(self, assistant: AssistantConfig):
#         self.assistant_list_base.append(assistant)
#
#     def create_assistant(self):
#         self.add_new_assistant(AssistantConfig(
#             name=input("who is your assistant?: "),
#             _description=input("Describe your assistant : ")))
#         return
#
#     def show_base_name(self):
#         return [user.name for user in self.assistant_list_base]
#
#     def show_all_configs(self):
#         return self.assistant_list_base
#
#
# mvp_1_assistant_base = AssistantBase('base_1')
#
#
# class UsersBase:  # aggregates
#
#     def __init__(self, name_base: UserConfig):
#         self.name_base = name_base
#         self.users_list_base = []
#         self._current_choice = None
#
#     @property
#     def _choice(self, user: UserConfig) -> None:
#         self._current_choice = user
#
#     def add_new_user(self, user: UserConfig):
#         self.users_list_base.append(user)
#
#     def create_new_user(self):
#         self.add_new_user(UserConfig(
#             name=input("who are You?: "),
#             _description=input("Get more infor about: ")
#         ))
#
#     def show_base_name(self):
#         return [user.name for user in self.users_list_base]
#
#     def show_all_configs(self):
#         return self.users_list_base
#
#
# class Interviewer:
#     assistant = AssistantBase.choice()
#     user = UsersBase.choice.choice()
#     config = [
#         dict(role="system", content=assistant.context),
#         dict(role="user", content=user.context)]
#
#
# class CustomChatGPT:
#     def __init__(self, assistant: AssistantConfig):
#         self.assistant = assistant
#         self.message_history = assistant.config_dict
#         self.tokens_have = 4097  # TODO: make more flexability
#
# # class BasicChatConfig:
# #     def __init__(self, list_api):
# #         self.list_api = list_api
# #
# #         self.current_db = None
# #         self.current_assistant = None
# #         self.basic_chat = None
# #         openai.api_key = self.list_api[0]  # revolder
# #
# #     def use_db(self, assistant_base: AssistantBase):
# #         self.current_db = assistant_base
# #         return self
# #
# #     def add_new_assistant(self, assistant: AssistantConfig):
# #         self.current_db.add_new_assistant(assistant)
# #         self.current_assistant = assistant
# #         return self


# save parameters to database
# participant_dict =  {
#     'user': UserConfig(
#     name="",
#     _description=''),
#     
# }
# 
class CreateNewParticipant:

    def create_new(self,type_config,name,_description):
        type_config(
            name=name,
            _description=_description)


nick_developer = UserConfig(
    name="nick",
    _description='Junior Python developer')

print(nick_developer.pre_text)

senior_python = AssistantConfig(
    name="senior_python",
    _description='Senior Python developer',
)
print(senior_python.pre_text)
ifrs = TopicConfig(
    name="ifrs",
    _description='About FRS'
)
print(senior_python.pre_text)
print(ifrs.message_history)
