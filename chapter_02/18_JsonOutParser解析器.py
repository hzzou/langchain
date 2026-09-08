import os

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv(verbose=True)
api_key = os.getenv('DEEPSEEK_API_KEY')
base_url = os.getenv('DEEPSEEK_BASE_URL')

str_parser = StrOutputParser()
json_parser = JsonOutputParser() # 把json字符串解析为dict字典


model = ChatOpenAI(
    model='deepseek-v4-flash',
    api_key=api_key,
    base_url=base_url,
)

# 换行不能有逗号，然后两个自动拼接为字符串。有逗号就成了元组
first_prompt = PromptTemplate.from_template(
    '我领居姓：{lastname}，刚生了个{gender}，请帮忙起名，并封装到JSON格式返回给我。'
    '要求key是name，value就是起的名字。请严格遵守格式要求'
)

second_prompt = PromptTemplate.from_template(
    '姓名{name}，请帮我解析含义'
)
                            # 把json解析为字典 {'name': '张若溪'}
chain = first_prompt | model | json_parser | second_prompt | model | str_parser

# res = chain.invoke({'lastname': '张', 'gender': '女儿'})
#
# print(res)

res = chain.stream({'lastname': '张', 'gender': '女儿'})

for chunk in res:
    print(chunk, end='', flush=True)
