import os, json
from typing import Sequence
from langchain_core.messages import message_to_dict, messages_from_dict, BaseMessage
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory

# message_to_dict(): 这里是to，把消息转为字典： 单个消息对象(BaseMessage类实例) -> 字典
# messages_from_dict(): 这里是from，把字典转为消息： [字典、字典、字典] -> [消息、消息、消息]
# AIMessage、HumanMessage、SystemMessage 都是BaseMessage的子类

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableWithMessageHistory


# 长期会话类
class FileChatMessageHistory(BaseChatMessageHistory):

    # 初始化赋值
    def __init__(self, session_id, storage_path):
        self.session_id = session_id      # 会话id
        self.storage_path = storage_path  # 不同会话id的存储文件所在的文件夹路径

        # 完整的文件路径拼接
        self.file_path = os.path.join(self.storage_path, self.session_id)

        # 确保文件夹是存在的
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    # 重写消息写入，注意带s
    def add_messages(self, messages: Sequence[BaseMessage]):

        all_messages = list(self.messages)   # 已有的消息列表
        all_messages.extend(messages)                     # 新的消息添加进all_messages

        # 将数据同步写入到本地文件中
        # 类对象写入文件 -> 一堆二进制
        # 为了方便，可以将BaseMessage消息转为字典（借助json模块以json字符串写入文件）
        # 官方message_to_dict:单个消息对象(BaseMessage类实例) -> 字典
        # new_messages = []
        # for message in all_messages:
        #     d = message_to_dict(message)
        #     new_messages.append(d)

        new_messages = [ message_to_dict(message) for message in all_messages] # 注意是in all_messages

        # 将文件写入文件, 把文件路径打开为f
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(new_messages, f, ensure_ascii=False, indent=4) # 是否转化ascii, 文件缩进indent,


    # @property 装饰器是将方法变成成员属性使用
    @property
    def messages(self) -> list[BaseMessage]:
        # 当前文件内: list[字典]
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                messages_data = json.load(f)  # 返回值就是list[字典]
                return messages_from_dict(messages_data)
        except FileNotFoundError:
            return []

    # 清空
    def clear(self) -> None:
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump([], f)

load_dotenv(verbose=True)

api_key = os.getenv('DEEPSEEK_API_KEY')
base_url = os.getenv('DEEPSEEK_BASE_URL')

model = ChatOpenAI(
    model='deepseek-v4-flash',
    api_key=api_key,
    base_url=base_url,
)

prompt = ChatPromptTemplate.from_messages(
    [
        ('system','你需要根据会话回应用户问题。对话历史，'),
        MessagesPlaceholder('chat_history'),  # 没有 {}
        ('human', '请回答如下问题，{input}'),    # 有{}
    ]
)

str_parser = StrOutputParser()

def print_prompt(full_prompt):
    print('='*20, full_prompt.to_string(), '='*20)

    return full_prompt


# 实现通过会话id把文件保存本地
def get_history(session_id):
    return FileChatMessageHistory(session_id, './chat_history')

# # 临时内存会话记忆
# store = {}
# def get_history(session_id):
#     if session_id not in store:
#         store[session_id] = InMemoryChatMessageHistory() # 开辟内存空间
#
#     return store[session_id]

# 基础链
base_chain = prompt | print_prompt |  model | str_parser


# 实现带历史会话的记忆链
conversation_chain = RunnableWithMessageHistory(
    base_chain,
    get_history,
    input_messages_key='input',
    history_messages_key='chat_history',
)

if __name__ == '__main__':
    session_config = {
        'configurable': {
            'session_id': 'user_02'
        }
    }

    # # 第一次
    # res = conversation_chain.invoke({'input': '小明有两只猫'}, config = session_config)
    #
    # print(res)
    #
    # # 第二次
    # res = conversation_chain.invoke({'input': '小张有一只狗'}, config = session_config)
    #
    # print(res)

    # 第三次， 有本地缓存时会加载本地缓存，所以不需要第一二次，即它们只需要执行一次
    res = conversation_chain.invoke({'input': '总共有几只宠物'}, config = session_config)

    print(res)



