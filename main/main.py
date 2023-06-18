import openai

openai.api_key = "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"


roles = [
    'system','user','assistant'
]

# def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301"):
#   """Returns the number of tokens used by a list of messages."""
#   try:
#       encoding = tiktoken.encoding_for_model(model)
#   except KeyError:
#       encoding = tiktoken.get_encoding("cl100k_base")
#   if model == "gpt-3.5-turbo-0301":  # note: future models may deviate from this
#       num_tokens = 0
#       for message in messages:
#           num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
#           for key, value in message.items():
#               num_tokens += len(encoding.encode(value))
#               if key == "name":  # if there's a name, the role is omitted
#                   num_tokens += -1  # role is always required and always 1 token
#       num_tokens += 2  # every reply is primed with <im_start>assistant
#       return num_tokens
# #   else:
# #         raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.

# print(f"{num_tokens_from_messages(messages, model)} prompt tokens counted.")



# example token count from the OpenAI API
import openai

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = message
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

# response = openai.ChatCompletion.create(
#     model=model,
#     messages=messages,
#     temperature=1,
# )

print(f'{response["usage"]["prompt_tokens"]} prompt tokens used.')
 I have list of handlers for dataframe like: 
```
def only_10(df): # handler first
    handle = df['form_type'].str.contains('10')
    df = df.query("@only_10")
    return df
def make_clases_from_columns(df): # handler second
    name_, type_,cik_,date_, f_name_ = (df[x] for x in df.columns)
```
And I want make a class, ProcessingTool what aggregate handlers, like:
``` class ProcessTool:
    def __init__(self,handlers:List):
        self.handlers = handlers
    def processing(self,df):
        ....
   
```
1. ProcessTool.processing must return reduce fucntion what  recurse return chanched df
2. Function declaration must example:
financials_reports = ProcessTool(hanlders=[only_10,make_clases_from_columns])
3. how I can Design Patterns approach
Show me how I can do it



'''
 I have list of handlers for dataframe like: 
```
def only_10(df): # handler first
    handle = df['form_type'].str.contains('10')
    df = df.query("@only_10")
    return df
def make_clases_from_columns(df): # handler second
    name_, type_,cik_,date_, f_name_ = (df[x] for x in df.columns)
```
And I want make a class, ProcessingTool what aggregate handlers, like:
``` class ProcessTool:
    def __init__(self,handlers:List):
        self.handlers = handlers
    def processing(self,df):
        ....
   
```
1. ProcessTool.processing must return reduce fucntion what  recurse return chanched df
2. Function declaration must example:
financials_reports = ProcessTool(hanlders=[only_10,make_clases_from_columns])
3. how I can Design Patterns approach
Show me how I can do it

'''
Topic : Study Japan for beginner step by step
Native laguage : russian
Task: create Plan for study and display in Table
Table columns:
- Study block : example("basic construction","main phrase",etc.)
-  Books: authors,name and relize date
- youtube channel links
- free courses links
'''




def CustomChatGPT(user_input):

    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = message
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    # print(f'{response["usage"]["prompt_tokens"]} prompt tokens used.')
    # with open(r"C:\Users\nickl\My_softwares\Own_Packacges\chatgpt_assistant\main\chat_file.csv","a+",encoding="utf-8") as f:

    #     f.write(f"\n{messages}")
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Data Science Developer")

demo.launch(share=True)