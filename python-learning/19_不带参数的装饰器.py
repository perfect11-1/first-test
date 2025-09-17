def my_decorator(func):
    def wrapper():
        print('在原函数之前执行')
        func() # 调用被装饰的函数
        print('在原函数之后执行')
    return wrapper # 返回装饰器函数

@my_decorator
def say_hello():   # 被装饰的函数
    print("Hello!我是被装饰前的输出")   

say_hello()  # 调用被装饰的函数(say_hello),实际是运行最终装饰器函数wrapper
# 输出:
# 在原函数之前执行
# Hello!我是被装饰前的输出
# 在原函数之后执行




