import os

from langchain_core.prompts import ChatPromptTemplate, ChatMessagePromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(verbose=True)

api_key = os.getenv('ZHIPU_API_KEY')
base_url = os.getenv('ZHIPU_BASE_URL')

client = ChatOpenAI(
    model='glm-5.3',
    api_key=api_key,
    base_url=base_url
)


# ChatMessagePromptTemplate是聊天一条信息模板
# 是聊天提示词模板ChatPromptTemplate总容器
chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ('system', '你是一个边塞诗人'),
        MessagesPlaceholder('history'), # 到时候需要注入的历史记录占位
        ('human', '请再来一首唐诗'),      # 最后让它再作一首
    ]
)

# 要注入的历史记录
history_data = [
    ('human', '你来写一首唐诗'),
    ('ai', '床前明月光，疑是地上霜，举头望明月，低头思故乡。'),
    ('human', '好诗再来一个'),
    ('ai', '锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦。')
]

# 需要转换为string
prompt_text = chat_prompt_template.invoke({'history': history_data}).to_string()

print(prompt_text)

res = client.invoke(input=prompt_text)

print(res.content)

