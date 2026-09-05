import numpy as np


"""
余弦相似性：即余弦值，越趋近1越相似，越趋近0越不相似
a . b/ |a||b|
"""



# 计算两个向量的点积，两个向量同维度数字乘积之和，即x1x2+y1y2或者x1x2x3+y1y2y3
def get_dot(vec_a, vec_b):
    if len(vec_a) != len(vec_b):
        raise ValueError("两个向量必须维度数量相同")

    dot_sum = 0
    for a, b in zip(vec_a, vec_b):
        dot_sum += a * b

    return dot_sum

# 计算向量模长 x*x + y*y 然后开平方
def get_norm(vec):
    sum_square = 0
    for a, b in zip(vec, vec):
        sum_square += a * b

    return np.sqrt(sum_square) # 开根号

# 计算余弦相似性
# 两个向量的点积除以两个向量模的乘积
def cosine_similarity(vec_a, vec_b):
    result = get_dot(vec_a, vec_b) / (get_norm(vec_a) * get_norm(vec_b))
    print(result)


if __name__ == '__main__':
    a = [1, 2, 3]
    b = ['x', 'y', 'z']

    res = zip(a, a)
    sum_square1 = 0
    for x, y in res:
        print(x, y)
        sum_square1 += x * y

    print(sum_square1)

    vec_a = [0.5, 0.5]
    vec_b = [0.7, 0.7]
    vec_c = [0.7, 0.5]
    vec_d = [-0.6, -0.5]

    print('余弦相似性:')
    cosine_similarity(vec_a, vec_b)
    cosine_similarity(vec_a, vec_c)
    cosine_similarity(vec_a, vec_d)
