import os

from langchain_community.document_loaders import CSVLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from dotenv import load_dotenv



load_dotenv(verbose=True)


api_key = os.getenv("QIANWEN_API_KEY")

dash_embed = DashScopeEmbeddings(
    dashscope_api_key=api_key,
)

# print(dash_embed.embed_query("我喜欢你"))

vector_store = InMemoryVectorStore(embedding=dash_embed)



loader = CSVLoader(
    file_path='./data/stu.csv',
    encoding='utf-8',
    csv_args={
        "delimiter" : ",",
        "quotechar" : '"',
        "fieldnames": ["name", "age", "gender", "hobby"]
    },
    # source_column='hobby', # 指定解析的加载数据来源，也就是metadata的source的字段值，默认则是整个文件，可选文件下的不同列的字段名
)

docs = loader.load()

# for doc in docs:
#     print(doc)

# 文本数学向量化
vector_store.add_documents(
    documents=docs,
    ids = ["id_"+str(i) for i in range(1, len(docs)+1)]
)

# print(vector_store.store)

# 检索， 返回list[Document]
result = vector_store.similarity_search(
    "刘",
    3    # 检索结果要几个
)

print(result)


