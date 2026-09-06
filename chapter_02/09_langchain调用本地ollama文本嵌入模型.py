import os

from langchain_ollama import OllamaEmbeddings
import ollama
from dotenv import load_dotenv

# 加载环境变量，以.env文件为准
load_dotenv(verbose=True)

# 调用load_dotenv()后才能使用os.getenv()
base_url = os.getenv('OLLAMA_EMBED_URL')

# dimensions指定向量维度
# 可以不传base_url
embed = OllamaEmbeddings(model='qwen3-embedding:4b', dimensions=1024, base_url=base_url)

print(embed.embed_query('你是'))
# embed = ollama.embed(model='qwen3-embedding:4b', input='你是')
#
# print(embed.embeddings)