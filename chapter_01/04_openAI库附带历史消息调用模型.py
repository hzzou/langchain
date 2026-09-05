from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama'
)

resp = client.chat.completions.create(
    model='qwen3:4b',
    messages=[
        {'role': 'system', 'content': '你是一个简洁的编程专家'},
        {'role': 'user', 'content': '小明有三只宠物狗'},
        {'role': 'pro', 'content': '好的'},
        {'role': 'user', 'content': '小红有两只宠物猫'},
        {'role': 'pro', 'content': '好的'},
        {'role': 'user', 'content': '总共有几只宠物'}
    ],
    stream=True
)

for chunk in resp:
    print(
        chunk.choices[0].delta.content,
        end=' ',
        flush=True
    )