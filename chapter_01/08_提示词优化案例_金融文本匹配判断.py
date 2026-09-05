from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama'
)

# 训练层数据
# []列表 ()元组
exam_data = {
    "是": [
        ("公司ABC发布了季度财报，显示盈利增长。", "财报披露，公式ABC利润上升。"),
        ("公司ITCAST发布了年度财报，显示盈利大幅增长。", "财务披露，公司ITCAST更赚钱了")
    ],
    "不是": [
        ("黄金价格下跌，投资者抛售。", "外汇市场交易额创下新高。"),
        ("央行降息，刺激经济增长。", "新能源技术的创新")
    ]
}

# 提示层，提问数据
questions = [
    ("利率上升，影响房地产市场。", "高利率对房地产有一定的冲击。"),
    ("油价大幅度下跌，能源公司面临挑战。", "未来智能城市的建设趋势越加明显。"),
    ("股票市场今日大涨，投资者乐观。", "持续上涨的市场让投资者感到满意。")
]

messages = [
    {'role': 'system', 'content': '帮我完成文本匹配，我给你两个句子，被[]包围，判断他们是否匹配，回答是或不是，请参考如下示例：'}
]

# 预训练层
# 给大模型问答示例，即Few-shot
for key, arr in exam_data.items():
    for t in arr:
        # 示例问的内容
        messages.append({'role': 'user', 'content': f"句子1：[{t[0]}]，句子2：[{t[1]}]"})
        # key 为 是或不是
        messages.append({'role': 'assent', 'content': key})

for item in messages:
    print(item)

# 模型提示词层
# 向模型提示的时候，一般要给它说，按照上述描述，如何操作后面的
for t in questions:
    res = client.chat.completions.create(
        model='qwen3:4b',
        messages=messages+[{'role': 'user', 'content': f'按照上述描述，回答这两个句子的情况。句子1：[{t[0]}]，句子2：[{t[1]}]'}]
    )

    print(res.choices[0].message.content)