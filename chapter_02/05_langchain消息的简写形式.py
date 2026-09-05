from langchain_ollama import ChatOllama

client = ChatOllama(model='transkatgirl/Qwen3-4B-Base:latest')

# 准备消息, 简写形式
# 动态的，在运行时由langchain内部机制转换为Message类对象
# 也可以支持内部{变量}占位
messages = [
    # (角色，内容) 角色：system/human/ai
    ('system', '你是一个边塞诗人'),
    ('human', '写一首诗'),
    ('ai', '锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦。'),
    ('human', '按照你上一个回复的格式，再写一首唐诗')
]

res = client.stream(input=messages)

for chunk in res:
    print(chunk.content, end='', flush=True) # 流式输出就不用每个文字换行, flush是不用缓存
    # print(chunk.content, flush=True) # 流式输出就不用每个文字换行, flush是不用缓存