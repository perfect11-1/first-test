def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs) # 调用被装饰的函数
        return wrapper  #返回的初始装饰器函数
    return decorator    #返回的最终装饰器函数


@repeat(3)
def say_hello(): #
    print("Hello!")

say_hello() #调用被装饰的函数(say_hello),实际是运行最终装饰器函数decorator
# 输出:
# Hello!
# Hello!
# Hello!