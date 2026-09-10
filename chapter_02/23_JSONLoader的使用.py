import json

from langchain_community.document_loaders import JSONLoader


loader = JSONLoader(
    file_path='./data/stus.json',
    jq_schema='.[].name',       # . 点是整个对象, .name是访问某个属性, .[].name是提取整个数组的某个属性， .other.addr是访问层级属性
    text_content=False,  # 解析的原文件是否是字符串json
    # json_lines=True      # json是否是多行
)

documents = loader.load()

print(documents)
# print(documents[0].page_content)