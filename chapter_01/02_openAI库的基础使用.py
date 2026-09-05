
from openai import OpenAI


# python里括号可以换行和加逗号
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama'
)

resp = client.chat.completions.create(
    model='qwen3:4b',
    messages=[
        # system 设定模型的行为和规则
        {'role': 'system', 'content': '你是简洁的编程助手'},
        # 设定模型的回答，由用户设定
        {'role': 'assistant', 'content': '好的，我是编程助手，并且是简洁的，你要问什么？'},
        # 用户的提问
        {'role': 'user', 'content': '写一段python读取csv的示例代码'}
    ],
)

print(resp.choices[0].message.content)