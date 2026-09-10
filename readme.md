
## 记录

* conda create —name langchain1.3 python=3.14.6 创建本地conda环境
* langchain-community: 社区支持包，提供更多的第三方模型调用 4b,sunset表示目前终止维护
* langchain-ollama: 基于ollama封装
* langchain-openai: deepseek依赖它，安装langchain-deepseek的时候会自动安装它 
* langchain_dashscope: 
* 国内厂商都做了兼容openai的接口，所以可以使用langchain-openai调用
* langchain-deepseek: 调用deepseek的依赖包
* dashscope: 千问的Python SDK
* chromadb: 轻量向数据库
* python-dotenv: 用于环境管理的包，类似于js中的dotenv，
* 使用的时候，from dotenv import load_dotenv，load_dotenv(verbose=True)，verbose=True表示以.env文件中为准
* 用python -m pip, 避免pip与python不同，使用清华的代理。python -m pip install chromadb -i https://pypi.tuna.tsinghua.edu.cn/simple
* langchain支持三种类型的模型：LLMs(大语言模型(底座))、Chat Models(聊天模型(Instruct))、Embeddings Models(嵌入模型)
* 创建csv文件时，在没有添加行和列，只有一个框的时候改csv文件格式可以，添加过后行或者列再改则不会生效，这是在pythCharm中，若以文本方式打开，则可以替换分隔符，即修改csv文件格式