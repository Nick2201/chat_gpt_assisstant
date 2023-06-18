from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List

from participants import TopicConfig
@dataclass
class LangModel:
    message_history : List = field(default_factory=list) # current message history

    def take_topic(self, topic: TopicConfig):
        message_history = topic.message_message_history
    @abstractmethod
    def connect_to_lm(self):
        ...

    @abstractmethod
    def ask_chat(self, user_input):
        return message


