from langchain_community.document_loaders import PyPDFLoader



loader = PyPDFLoader(
    file_path='../../你不知道的JavaScript01.pdf',
    mode='single'   # 默认是page模式，按pdf一页形成一个Document对象,single是直接一次形成一个Document对象
)

i = 0

for doc in loader.lazy_load():
    i += 1
    print(doc)
    print("="*30, i)