import os

from openai import OpenAI
import anthropic
from dotenv import load_dotenv


load_dotenv(verbose=True)

api_key = os.getenv('QIANWEN_API_KEY')
open_base_url = os.getenv('QIANWEN_OPENAI_BASE_URL')
claude_base_url = os.getenv('QIANWEN_CLAUDE_BASE_URL')

# # openai调用
# client = OpenAI(
#     api_key=api_key,
#     base_url=open_base_url,
# )
#
# res = client.responses.create(
#     model='qwen3.8-max',
#     input='你是谁？'
# )
#
# print(res.output_text)



# claude调用
client = anthropic.Anthropic(
    api_key=api_key,
    base_url=claude_base_url
)

res = client.messages.create(
    model='qwen3.8-max',
    max_tokens=1024,
    messages=[
        {'role': 'user', 'content': '你是谁？'}
    ],
)

print(res)

# 模型思考过程
print(res.content[0].thinking)

# 模型答案
print(res.content[1].text)