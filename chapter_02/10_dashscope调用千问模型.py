import os

import dashscope
from dotenv import load_dotenv
from dashscope import Generation

load_dotenv(verbose=True)

api_key = os.getenv('QIANWEN_API_KEY')
api_url = os.getenv('QIANWEN_DASHSCOPE_BASE_URL')

print(api_key)
print(api_url)

dashscope.api_key = api_key
dashscope.base_http_api_url = api_url



res = Generation.call(
    model='qwen3.7-max',
    max_tokens=1024,
    messages=[
        {'role': 'user', 'content': '你是谁'}
    ],
    result_format='message'
)

# 需要灵活获取属性
print(res.output.choices[0].message.content)

