
from langchain_ollama import OllamaLLM



res = OllamaLLM(model='transkatgirl/Qwen3-4B-Base:latest')

stream = res.stream(input='你是谁？')

for chunk in stream:
    print(chunk, end= '', flush=True)