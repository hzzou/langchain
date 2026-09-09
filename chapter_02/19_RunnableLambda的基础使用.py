import os

from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda


load_dotenv(verbose=True)

api_key = os.getenv('DEEPSEEK_API_KEY')
base_url = os.getenv('DEEPSEEK_BASE_URL')

model = ChatOpenAI(
    model='deepseek-v4-flash',
    api_key=api_key,
    base_url=base_url,
)

str_parser = StrOutputParser()
json_parser = JsonOutputParser()

first_template = PromptTemplate.from_template(
    '我领居姓：{lastname}，刚生了{gender}，请帮忙起名字，仅生成一个名字，不需要额外信息。'
)

second_template = PromptTemplate.from_template(
    '姓名{name}，请帮忙解析含义。'
)

# 自定义函数
func = RunnableLambda(lambda msg: {'name': msg.content})

chain = first_template | model | func | second_template | model | str_parser

# res = chain.invoke({'lastname': '张', 'gender': '女儿'})

# print(res)

res = chain.stream({'lastname': '张', 'gender': '女儿'})

for chunk in res:
    print(chunk, end='', flush=True)
