import os

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv(verbose=True)

api_key = os.getenv('DEEPSEEK_API_KEY')
base_url = os.getenv('DEEPSEEK_BASE_URL')

model = ChatOpenAI(
    model='deepseek-v4-flash',
    api_key=api_key,
    base_url=base_url,
)


# 普通字符串模板
# prompt = PromptTemplate.from_template(
#     '你需要根据会话历史回应用户问题。对话历史：{chat_history}，用户提问：{input}，请回答。'
# )

# 默认生成的聊天信息用户模板
template = ChatPromptTemplate.from_template('测试数据')

print(template)

# 是生成历史聊天记录
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', '你需要根据会话回应用户问题。对话历史,'),
        MessagesPlaceholder('chat_history'),  # 没有 {}
        ('human', '请回答如下问题，{input}'),
        template
    ]
)

str_parser = StrOutputParser()

def print_prompt(full_prompt):
    print('='*10, full_prompt.to_string(), '='*10)

    return full_prompt

# 先构建的基础链
base_chain = prompt | print_prompt | model | str_parser

store = {}

# 实现通过会话id获取InMemoryChatMessageHistory类对象
def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory() # 开辟内存空间

    return store[session_id]

# 实现带历史会话记忆链
conversation_chain = RunnableWithMessageHistory(
    base_chain,      # 被增强的原有基础链
    get_history,     # 通过会话id获取InMemoryChatMessageHistory类对象
    input_messages_key='input',    # prompt里的占位符
    history_messages_key='chat_history' # prompt里的占位符
)


if __name__ == '__main__':
    session_config = {
        'configurable': {
            'session_id': 'user_01'
        }
    }
    res = conversation_chain.invoke(input={'input': '小明有两个猫'}, config=session_config)

    print(res)

    res_1 = conversation_chain.invoke(input={'input': '小张有1只小狗'}, config=session_config)

    print(res_1)

    res_2 = conversation_chain.invoke(input={'input': '总共有几只宠物'}, config=session_config)

    print(res_2)

