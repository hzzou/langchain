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
    # source_column='hobby', # 每一行的唯一标识自定义指定是这行的哪列字段，不指定就是metadata_source
)

docs = loader.load()

# for doc in docs:
#     print(doc)


vector_store.add_documents(
    documents=docs,
    ids = ["id_"+str(i) for i in range(1, len(docs)+1)]
)

print(vector_store)

# 检索， 返回list[Document]
result = vector_store.similarity_search(
    "刘",
    3    # 检索结果要几个
)

print(result)


