try:
    # 可能会出错的代码
    x = int(input("请输入一个整数: "))
    result = 8 / x
    print(result)
except ValueError:
    # 处理 ValueError 异常
    print("输入的不是整数，请输入一个整数")
except ZeroDivisionError:
    # 处理 ZeroDivisionError 异常
    print("除零错误，请输入一个非零整数")
except Exception as e:
    # 处理其他异常
    print(f"发生未知错误: {e}")
else:
    # 如果没有异常发生，执行这里的代码
    print("程序运行正常")
finally:
    # 无论是否发生异常，都会执行这里的代码
    print("程序结束")