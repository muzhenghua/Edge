import os


class function:
    _list = []

    def __init__(self, a):
        self.a = a
        pass

    # 静态方法就是一个函数，可不用实例化就调用，无法调用类方法和类属性
    @staticmethod
    def get_info(a):
        # print(self.a) # 报错无法使用
        # self.__get_info_private()  # 报错无法使用

        a = a + 'ss'
        print('print')
        return a

    # 类方法，可以直接调用，不用实例化，也可实例化调用，无法调用类方法和类属性。
    @classmethod
    def get_info_class_method(cls):
        # print(self.a) # 报错
        # 会报错missing 1 required positional argument: 'self'
        cls.__get_info_private()
        print(cls.get_info('ss'))
        print('class method')

    # 通常针对同名函数的自定义操作
    def _get_info_class_method(self):
        print(self.a + 'class method' + '_')
        return self.a + 'class method' + '_'

    # 类实例方法，不接收参数，仅供内部调用。
    def get_info_method(self, a):
        print('method')
        print(a)
        self.__get_info_private()
        return self.a + 'method'

    # 内部函数,仅供内部调用。函数外部无法直接使用，但是可通过调用内部函数间接调用
    def __get_info_private(self):
        print(self.a + ' private method')
        return self.a + 'private method'

    # 类变量在类里面共享值，被修改后其他地方使用值也会被修改
    def modify_v_a(self):
        self.a += self.a

    def _modify_v_a(self):
        self.a += self.a


# function.get_info_class_method()
# function.get_info('ss')

# func = function(a='ss')
# # func.get_info_method('ss')
# # func.get_info('ss')
# # func.get_info_class_method()
# # func._get_info_class_method()
# func.modify_v_a()
# func._modify_v_a()
# print(func.a)
# func1 = function(a='aa')
# func._list.append('ssss')
#
# print(func._list)
# print(func1._list)


def get_pararmeter(*args, **kwargs):
    print(args)  # 不定长参数，他可以表示输入参数是不确定的，可以是任意多个。
    print(kwargs)  # 关键字参数，赋值的时候是以键= 值的方式


get_pararmeter(['ss', 'ss'])

a = 1
c = [a]
a = 2
print(c)
print(dir(a))
ab = [lambda x: x * x[0, 1, 2]]
print(ab)


def multipliers1():
    # 闭包,返回的四个函数， 
    a = [lambda x: i * x for i in range(4)]
    print(a)
    print('=====')
    return a


a = multipliers1()
for i in a:
    print(i(10))

# print([m(2) for m in a])
