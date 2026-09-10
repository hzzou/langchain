from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter  # text递归分割符



loader = TextLoader('./data/python基础语法.txt', encoding='utf-8')

docs = loader.load()

spliter = RecursiveCharacterTextSplitter(
    chunk_size=500,      # 分段的最大字符数
    chunk_overlap=50,    # 分段之间允许重叠的字符数
    # 文本自然段落的依据符合
    separators=["\n\n", "\n", "。", "！", "？", ".", "?", "!", " ", ""],
    length_function=len    # 统计字符用的函数
)

split_docs = spliter.split_documents(docs)

print(split_docs)
print(len(split_docs))

for doc in split_docs:
    print("="*20)
    print(doc)
    print("=" * 20)