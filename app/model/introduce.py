from dataclasses import dataclass

from participants import AssistantConfig, UserConfig



class AssistantBase:
    def __init__(self,name_base):
        self.name_base = name_base
        self.users_list_base = []

    def add_new_assistant(self,new_user:AssistantConfig):
        self.users_list_base.append(new_user)

    def create_new_user(self):
        name = input("who is your assistant?: ")
        config_dict_ = [
            {"role":"system",
            'content':input("Describe your assistant : ")},
            {"role": "user",
            'content':input("who are you?: ")}]
        self.add_new_assistant(AssistantConfig(name=name,config_dict=config_dict_))
    def show_base_name(self):
        return [user.name for user in self.users_list_base]
    def show_all_configs(self):
        return self.users_list_base
