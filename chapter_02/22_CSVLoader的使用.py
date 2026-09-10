from langchain_community.document_loaders import CSVLoader



loader = CSVLoader(
    file_path='./data/stu.csv',
    csv_args={
        'delimiter': ';',
        'quotechar': '"',
        'fieldnames': ['a', 'b', 'c', '爱好']
    },
    encoding='utf-8'
)


# documents = loader.load()
#
# print(documents)
#
# for document in documents:
#     print

for document in loader.lazy_load():
    print(document)