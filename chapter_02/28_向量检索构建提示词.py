import os

from dotenv import load_dotenv
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import ChatOpenAI

load_dotenv(verbose=True)


api_key = os.getenv('QIANWEN_API_KEY')
base_url = os.getenv('QIANWEN_OPENAI_BASE_URL')

str_parser = StrOutputParser()

dash_embed = DashScopeEmbeddings(
    dashscope_api_key=api_key,
)

vector_store = InMemoryVectorStore(embedding=dash_embed)

model = ChatOpenAI(
    api_key=api_key,
    base_url=base_url,
    model='qwen3.8-max',
    max_tokens=1024,
)

# 提示词
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', '以我提供的已知参考资料为主，简洁和专业的回答用户的问题。参考资料：{context}'),
        ('user', '用户提问：{input}')
    ]
)

# 准备一下资料(向量库的数据)
# 向向量库手动传入的一个list[str]
vector_store.add_texts(['减肥就是要少吃多练', '在减脂期间吃东西很重要，清淡少油控制卡路里摄入并运动起来', '跑步是很好的运动哦'])

# 用户的输入
input_text = '怎么减肥？'

# 检索向量库
result = vector_store.similarity_search(input_text, 2 )

print(result)

# 构建参考资料
reference_text = '['
for doc in result:
    reference_text += doc.page_content
reference_text += ']'

# 打印提示词
def print_prompt(prompt):
    print(prompt.to_string())
    print("="*50)
    return prompt


# 构建链
chain = prompt | print_prompt | model | str_parser

# 先检索出数据，然后组装起来给模板
res = chain.invoke({'input': input_text, 'context': reference_text})

print(res)

