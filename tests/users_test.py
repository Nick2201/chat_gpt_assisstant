import os
# from app.model import UsersBase,UserConfig
# def test_base():
#     '''
#     1. create new base
#     2. add new user in base
#         2.1 imput window
#     3. show
#     '''
#     developer = UserConfig(
#             name="user_developer",
#             config_dict= [{"role": "system",
#                 'content': f"You are Pythin Senior developer. \
#                 After your solution, you need write block '[commets]' and add some example below"},
#             {"role": "user",
#                 "content":"I'm Junior developer and study in job" }])

#     user_base_v_1 = UsersBase(name_base='base_v1.0')
#     user_base_v_1.add_new_user(developer)
#     print(user_base_v_1.show_base_name())

#     user_base_v_1.create_new_user()
#     print(user_base_v_1.show_base_name())
#     print(user_base_v_1.show_all_configs())
# test_base()


# list_api = open("key.txt", "r").read().strip("\n").split("\n")

print(os.getenv('API_KEYS'))