
## 记录

* base是大模型底座，Instruct是训练后的聊天模型
* 报错NameError: name 'dashscope' is not defined不是说没定义dashscope，而是说这个区域没定义某个你写的字段
* or是逻辑或，| 是按位或
* format方法入参是关键字参数，返回普通字符串
* invoke入参是字典，返回的是StringPromptValue对象
* 只有原生的OpenAI()在构建时，是把api_key/base_url和model分开设置
* 其余的二次封装都是把它们api_key、base_url、model全部放在同一个类的初始化构造函数里
* chain = prompt_template | model   此处的model是加了api_key和base_url的，有时也命名为client