import os
from langchain_chroma import Chroma
from dotenv import load_dotenv
from langchain_community.document_loaders import CSVLoader
from langchain_community.embeddings import DashScopeEmbeddings


load_dotenv(override=True)

api_key = os.getenv('QIANWEN_API_KEY')

dash_embed = DashScopeEmbeddings(
    dashscope_api_key=api_key,
)

# Chroma 向量数据库(轻量级)
# 确保chromadb langchain-chroma这两个库已安装
vector_store = Chroma(
    collection_name='test',             # 当前向量存储的名字
    embedding_function=dash_embed,      # 嵌入模型
    persist_directory='./chroma_db',    # 指定数据存放的文件夹
)

#
# loader = CSVLoader(
#     file_path='./data/stu.csv',
#     encoding='utf-8',
#     csv_args={
#         'delimiter': ',',
#         'quotechar': '"',
#         'fieldnames': ['name', 'age', 'gender', 'hobby']
#     },
#     source_column='age'     # 指定metadata里source字段的数据来源，默认则是整个文件，可指定csv文件的不同字段
# )
#
# docs = loader.load()
#
# print(docs)
#
# vector_store.add_documents(
#     documents=docs,
#     ids=["id_"+str(i) for i in range(1, len(docs)+1)]
# )

# 只要加载一次就用数据库缓存里
result = vector_store.similarity_search(
    "刘",  # 查询内容
    3,        # 检索结果要几个
    filter={"source": "22"}         # 此处source就是就是metadata的source字段
)

print(result)

print(vector_store._collection.count())  # 查看vector_store有几条数据

#vector_store.delete(['id_1'])

#print(vector_store._collection.count())