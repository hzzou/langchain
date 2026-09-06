import os
# langchain_community 已经终止维护，所以会看见运行警告
# from langchain_community.chat_models import ChatZhipuAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from openai import OpenAI
from zai import ZhipuAiClient
import anthropic

load_dotenv(verbose=True)

api_key = os.getenv('ZHIPU_API_KEY')
base_url = os.getenv('ZHIPU_BASE_URL')
claude_url = os.getenv('ZHIPU_CLAUDE_URL')

# # 这种模式已废弃
# client = ChatZhipuAI(
#     model='glm-5.3',
#     api_key=api_key,
#     #api_base=base_url,
# )
# res = client.invoke('请简要介绍一下你自己')
# print(res.content)

# # langchain上的openai 兼容模式调用，所有的ai都可以这样调用
# client = ChatOpenAI(
#     model='glm-5.3',
#     api_key=api_key,
#     base_url=base_url,
# )
#
# res = client.invoke('请简要介绍一下你自己')
#
# print(res.content)

# # 原生openai集成
# client = OpenAI(api_key=api_key, base_url=base_url)
#
# res = client.chat.completions.create(
#     model='glm-5.3',
#     messages=[{'role': 'user', 'content': '请介绍一下你是谁'}]
# )
#
# print(res.choices[0].message.content)

# # 使用官方python sdk调用
# client = ZhipuAiClient(api_key=api_key, base_url=base_url)
#
# res = client.chat.completions.create(
#     model='glm-5.3',
#     messages=[{'role': 'user', 'content': '请介绍一下你是谁'}]
# )
#
# print(res.choices[0].message.content)

# # Claude官方的框架
# client = anthropic.Anthropic(base_url=claude_url, api_key=api_key)
#
# res = client.messages.create(
#     model='glm-5.3',
#     max_tokens=1024, # 限制最大token
#     messages=[
#         {'role': 'user', 'content': '请简要介绍一下你自己'}
#     ]
# )
#
# # 此thinking属性需要根据框架实际情况查询
# print(res.content[0].thinking)

