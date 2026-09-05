from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama'
)

exam_data = {
    '新闻报道': '今日，股市经历了一轮震荡，受到宏观经济数据和全球贸易紧张局势的影响。',
    '财务报告': '本公司年度财务报告显示，去年公司实现了稳步增长的盈利，同时资产负债表呈现强劲的状况',
    '公司公告': '本公司高兴地宣布成功完成最新一轮交易，收购了一家在人工智能领域领先的公司',
    '分析师报告': '最新的行业分析报告指出，科技公司的创新将成为未来增长的主要推动力。'
}

exam_type = ['新闻报道', '财务报道', '公司公告', '分析师报告']

questions = [
    '今日，央行发布公告宣布降低利率，以刺激经济增长。',
    'ABC公司今日发布公告称，已成功完成对XYZ公司股权的收购的交易。',
    '公司资产负债表显示，公司偿债能力强劲，现金流充足，为未来投资和扩张提供了坚实的财务基础',
    '最新的分析报告指出，可再生能源行业预计将在未来几年经历持续增长，投资者应该关注这一领域的投资机会',
    '小明喜欢小星哟'
]

"""
[
    # 训练层数据
    {'role': 'system', 'content': '你是金融专家'},
    {'role': 'user', 'content': ''},
    {'role': 'assistant', 'content': ''},
    # 提示层数据
    {'role': 'user', 'content': '要提的问题'}
]
"""

messages = [
    {'role': 'system', 'content': '你是金融专家，将文本分类为["新闻报道", "财务报道", "公司公告", "分析师报告"]，不清楚的分类为"不清楚"类别'}
]

# 模型的训练层
# 把exam_data的装进messages里的role里
for key, value in exam_data.items():
    messages.append({'role': 'user', 'content': value})
    messages.append({'role': 'assistant', 'content': key})

# 模型的提示层
# 向模型提问
for q in questions:
    res = client.chat.completions.create(
        model='qwen3:4b',
        messages=messages+[{'role':'user', 'content': f"按照示例，回答这段文本的分类类别: {q}"}]
    )

    print(res.choices[0].message.content)