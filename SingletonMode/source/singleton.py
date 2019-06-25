# 单例模式实现日志记录


class SingletonLogging(object):
    class __SingletonLoggingReal():
        def __init__(self):
            self.value = None

        # 指向单例对象的指针，是一个类属性
        instance = None

        def __new__(cls):
            # 如果没有实例化对象，就实例化
            if SingletonLogging.instance is None:
                SingletonLogging.instance = SingletonLogging.__SingletonLoggingReal()
                return SingletonLogging.instance

        # def __getattr__(self, item):
        #     return getattr(self.instance, item)
        #
        # def __setattr__(self, value):
        #     return setattr(self.instance, value)


def test_singleton1():
    obj1 = SingletonLogging()
    obj1.value = 'i am 1'

    print(obj1, obj1.value)

    obj2 = SingletonLogging()
    obj2.value = 'i am 2'

    print(obj1, obj1.value)
    print(obj2, obj2.value)

# 下面有三种实现单例的方式
# 这里是参考
# https://foofish.net/python_singleton.html

################################################
# 使用基类实现单例模式
# 利用__new__
################################################


class MySingleton(object):

    def __new__(cls, *args, **kwargs):
        print('ok', cls)
        if not hasattr(cls, '_instance'):
            cls._instance = super(MySingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(MySingleton):

    def __init__(self):
        self.value = None


def test_singleton2():
    obj1 = MyClass()
    obj1.value = '1'

    print(obj1, obj1.value)
    print('_instance', obj1._instance)
    print('\n')

    # obj2 = MyClass()
    # obj2.value = '2'
    #
    # print(obj1, obj1.value)
    # print(obj2, obj2.value)
    #
    # print(obj1 is obj2)


################################################
# 使用修饰器实现单例模式
################################################

def my_singleton_decorator(cls):
    instance = {}

    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapper


@my_singleton_decorator
class MyClassDecorator(object):

    def __init__(self):
        self.value = None


def test_singleton_decorator():
    obj1 = MyClassDecorator()
    obj2 = MyClassDecorator()

    print(obj1 is obj2)


################################################
# 使用元类实现单例模式
################################################
class MySingletonOrigin(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(MySingletonOrigin, cls).__call__(*args, **kwargs)
        return cls._instance


class MyClassOrigin(object):
    __metaclass__ = MySingletonOrigin


def test_singleton_origin():
    obj1 = MyClassOrigin()
    obj2 = MyClassOrigin()
    print(obj1 is obj2)


if __name__ == '__main__':
    """"""
    # test_singleton1 # ❌
    test_singleton2() # ✅
    # test_singleton_decorator() # ✅
    # test_singleton_origin() # ❌
