
# 访问本地ollama
from langchain_ollama import OllamaLLM

ollama = OllamaLLM(model='transkatgirl/Qwen3-4B-Base:latest')

res = ollama.invoke('你是大模型基座还是聊天模型')

print(res)