import os

from langchain_community.embeddings import DashScopeEmbeddings
from dotenv import load_dotenv


load_dotenv(verbose=True)

api_key = os.getenv('QIANWEN_API_KEY')

print(api_key)

embed = DashScopeEmbeddings(
    dashscope_api_key=api_key
)

print(embed.embed_query("我喜欢你"))
print(embed.embed_documents(["你好", "再买"])) # aembed_documents()是他的异步，用在FAST_API项目中


# async def das():
#     m = await embed.aembed_documents(["你好", "再买"])
#     print(m)
