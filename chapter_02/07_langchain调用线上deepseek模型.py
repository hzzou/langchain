
import os  # 这是python内置标准模块Operating‑System

# langchain_deepseek基于langchain_openai，所以也可以使用ChatOpenAI调用
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain_openai import ChatOpenAI


# 加载全局.env文件环境变量，verbose=True表示若有相同以.env文件中的优先
load_dotenv(verbose=True)

# load_dotenv()调用之后, os.getenv()才能获取到它从.env加载环境变量
# 没有返回None,程序继续运行
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
deepseek_base_url = os.getenv("DEEPSEEK_BASE_URL") or ''

print(deepseek_api_key)
print(deepseek_base_url)

# 没有直接抛出错误
ds = os.environ.get("DEEPSEEK_API_KEY")
print(ds)


# deepseek = ChatDeepSeek(
#     model='deepseek-v4-flash',
#     api_key=deepseek_api_key,
#     base_url=deepseek_base_url
# )
#
#
# res = deepseek.invoke('请简短介绍你是谁')
#
# print(res.content)


client = ChatOpenAI(
    model='deepseek-v4-flash',
    base_url=deepseek_base_url,
    api_key=deepseek_api_key,
)

res = client.invoke('请简要介绍一下你是谁')

print(res.content)


