import os

from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Tongyi
from dotenv import load_dotenv

load_dotenv(verbose=True)

api_key = os.getenv('QIANWEN_API_KEY')
base_url = os.getenv('QIANWEN_DASHSCOPE_BASE_URL')

# PromptTemplate为zero-shot思想
# 设定模板
prompt_template = PromptTemplate.from_template(
    "我的领居姓{lastname}，刚生了{gender}, 你帮我起个名字，简单回答。"
)

# 调用format方法向模板注入信息 format方法入参是关键字参数，返回普通字符串
prompt_text = prompt_template.format(lastname='张', gender='女儿')

print(prompt_text)

# 使用社区的, 要注意这个sdk支持的model
client = Tongyi(
    model='qwen-plus',
    api_key=api_key,
    base_url=base_url,
)

# res = client.invoke(input=prompt_text)
#
# print(res)

# 链模式 构建执行链条
chain = prompt_template | client

# invoke入参是字典，返回的是StringPromptValue对象
res = chain.invoke(input={'lastname': '张', 'gender': '女儿'})

print(res)