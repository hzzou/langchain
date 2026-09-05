from openai import OpenAI

# 1.获取client对象，OpenAI类对象
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama'  # 可以随便填，但不能为空
)

# 2.调用模型
response = client.chat.completions.create(
    model='qwen3:4b',
    messages=[
        # system 设定模型的行为和规则
        {'role': 'system', 'content': '你是一个Python编程专家，并且话很多'},
        # 设定模型的回答，由用户设定
        {'role': 'assistant', 'content': '好的，我是编程专家，并且话很多，你要问什么？'},
        # 用户的提问
        {'role': 'user', 'content': '写一段python读取csv的代码'}
    ],
    stream=True # 开启了流式输出
)

# 3.处理结果 流式输出是一个字一个字的出
for chunk in response:
    print(
        chunk.choices[0].delta.content,
        end=' ',      # 每隔一段加空格
        flush=True    # 立刻刷新缓冲区
    )


