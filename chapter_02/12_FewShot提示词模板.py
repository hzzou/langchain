import os

from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(verbose=True)


api_key = os.getenv('QIANWEN_API_KEY')
base_url = os.getenv('QIANWEN_OPENAI_BASE_URL')

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
)




# 示例模板
exam_template = PromptTemplate.from_template('单词：{word}，反义词：{antonym}')

# 示例的动态数据
exam_data = [
    {'word': '大', 'antonym': '小'},
    {'word': '上', 'antonym': '下'}
]


few_template = FewShotPromptTemplate(
    examples=exam_data,                        # 示例数据
    example_prompt=exam_template,              # 示例模板
    prefix='告知我单词的反义词，我提供如下的示例：',  # 示例之前的提示词
    suffix='基于前面的示例告知我，{input_word}的反义词是？',  # 示例之后的提示词 此处预留插槽
    input_variables=['input_word'],                     # 此处预留变量插槽
)

# 调用to_string()格式化显示
prompt_text = few_template.invoke(input={'input_word': '左'}).to_string()

print(prompt_text)

res = client.responses.create(
    model='qwen3-max',
    input=prompt_text
)

#print(res)
print(res.output[0].content[0].text)