from langchain_ollama.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


# 得到模型对象
client = ChatOllama(model='transkatgirl/Qwen3-4B-Base:latest')
# client = ChatOllama(model='qwen3:4b')

# 准备消息列表
# 静态的，一步到位
messages = [
    SystemMessage(content='你是一个边塞诗人'),
    HumanMessage(content='写一首唐诗'), # 人让它写唐诗
    AIMessage(content='锄禾日当午，汗滴禾下土，水滴盘中餐，粒粒皆辛苦。'), # AI回答了这首唐诗
    HumanMessage(content='按照你的上一个回复的格式，再写一首唐诗。')
]

# 调用流式输出
res = client.stream(input=messages)

# for循环迭代打印输出
for chunk in res:
    print(chunk.content, end='', flush=True)