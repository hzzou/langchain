
## 记录

* base是大模型底座，Instruct是训练后的聊天模型
* 报错NameError: name 'dashscope' is not defined不是说没定义dashscope，而是说这个区域没定义某个你写的字段
* or是逻辑或，| 是按位或
* format方法入参是关键字参数，返回普通字符串
* invoke入参是字典，返回的是StringPromptValue对象
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
* 模型输出：AIMessage
* 提示词模板输入：字典，提示词模板输出：PromptValue对象
* InMemoryChatMessageHistory类对象是创建内存零时空间存储历史会话