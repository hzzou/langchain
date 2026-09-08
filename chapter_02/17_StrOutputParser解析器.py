import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv(verbose=True)

api_key = os.getenv('DEEPSEEK_API_KEY')
base_url = os.getenv('DEEPSEEK_BASE_URL')

model = ChatOpenAI(
    model='deepseek-v4-flash',
    api_key=api_key,
    base_url=base_url,
)

prompt = PromptTemplate.from_template(
    '我领居姓：{lastname}，刚生了{gender}，请起名，仅告知我名字无需其它内容。'
)

parser = StrOutputParser() # 把大模型的AIMessage剥离，直接得到str文本

print(prompt)
# # 没构建自动解析器
# chain = prompt | model
#
# res = chain.invoke({'lastname': '张', 'gender': '女儿'})
# # 需要手动打印content
# print(res.content)

chain = prompt | model | parser  # 构建解析器自动解析

res = chain.invoke({'lastname': '张', 'gender': '女儿'})

print(res) # 已经由paser自动解析，不需要打印content
print(type(res))