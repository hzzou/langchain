import json


class Test(object):
    # 构造方法是__new__
    # 初始化相关属性, 不返回相关值
    def __init__(self, name):
        self.name = name

    def __or__(self, other):
        return MySequence(self, other)

    # python的魔法方法返回它的名字，而非内存地址
    # def __str__(self):
    #     return self.name

    # 魔法方法，把内存地址还原为对象，没有__str__时，print会回退使用它
    def __repr__(self):
        return self.name

class MySequence(object):

    def __init__(self, *args):
        self.sequence = []
        for arg in args:
            self.sequence.append(arg)

    def __or__(self, other):
        self.sequence.append(other)
        return self  # 返回它自己，无限链接

    # 打印的是内存地址
    def run(self):
        for i in self.sequence:
            print(i)

    def __repr__(self):
        return str(self.sequence)


if __name__ == '__main__':
    a = Test('a')
    b = Test('b')
    c = Test('c')
    e = Test('e')
    f = Test('f')

    d = a | b | c | e | f

    d.run()
    print(type(d))
    print(d)

