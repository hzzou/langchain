
## 记录

* HumanMessage类对应简写 human/user
* AIMessage类对应简写 assistant/ai
* SystemMessage类对应简写 system
* ToolMessage类对应简写 tool 工具返回结果
* MessagesPlaceholder类对应简写 placeholder 历史对话列表消息占位
* base是大模型底座，Instruct是训练后的聊天模型
* 报错NameError: name 'dashscope' is not defined不是说没定义dashscope，而是说这个区域没定义某个你写的字段
* or是逻辑或，| 是按位或
* format方法入参是关键字参数，返回普通字符串，只是拼接字符串
* invoke入参是字典，返回的是StringPromptValue对象，会调用LLM
* 只有原生的OpenAI()在构建时，是把api_key/base_url和model分开设置
* 其余的二次封装都是把它们api_key、base_url、model全部放在同一个类的初始化构造函数里
* PromptTemplate.from_template 是普通字符串模板
* ChatPromptTemplate.from_template 是聊天信息用户模板
* ChatPromptTemplate.from_messages 是生成多条历史聊天记录
* chain = prompt_template | model   此处的model是加了api_key和base_url的，有时也命名为client, 是模板和大模型的运算
* 链的构建必须是chain = prompt | model | prompt | model, 不能是chain = prompt = prompt | model | model, 即模板和模型交替
* 链的构建也可以是chain = prompt | model | parser | model, parser是字符串解析器
* 只要继承来自Runnable对象，它们就可以就行按位或运算
* 上一个组件的输出即是下一个组件的输入，即prompt_template的输出即是model的输入
* __str__和__repr__在调用print和str()和format(), f'{obj}‘字符串格式化的时候会自动调用
* JsonOutputParser: AIMessage输入, 是把json字符串解析为dict字典
* StrOutputParser：AIMessage输入, 是把AIMessage剥离掉无用信息，直接输出str字符串有效信息
* model模型输出：AIMessage
* 提示词模板输入：字典，提示词模板输出：PromptValue对象
* InMemoryChatMessageHistory类对象是创建内存零时空间存储历史会话
* JSONLoader使用python库jq的解析语法，.表示根(整个对象)、[]表示数组、.name表示从根取name的值
* .hobby[1]表示取hobby对应数组的第二个元素、.[]表示将数组内的每个字典(JSON对象)都取到
* .[].name表示获取数组内每个字典(JSON)对象的name对应的值