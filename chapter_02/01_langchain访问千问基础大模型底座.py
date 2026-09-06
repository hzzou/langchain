# llms是指大模型的复数
import os

# langchain_community 已经终止维护，运行有警告
from langchain_community.llms import Tongyi
from dotenv import load_dotenv

load_dotenv(verbose=True)


api_key = os.getenv('DASHSCOPE_API_KEY')
base_url = os.getenv('DASHSCOPE_BASE_URL')


# 使用阿里通义千问(华北平台有免费额度)
res = Tongyi(
    model="qwen-plus",
    api_key=api_key,
    base_url=base_url
)


data = res.invoke("你是谁呀能做什么?")

print(data)