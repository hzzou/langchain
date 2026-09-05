import langchain

print(langchain.__version__)

import ollama


response = ollama.chat(
    model='qwen3:4b', # 实际本地部署的模型
    messages=[{'role': 'user', 'content': '介绍你自己'}]
)

# 访问的时候是message单数，不是开始定义时的chat()函数那里那样复数
print(response['message']['content'])