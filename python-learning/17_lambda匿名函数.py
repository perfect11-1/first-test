f = lambda x, y: x + y
print(f(1, 2))  # 输出: 3

x = lambda a, b: a * b
print(x(5, 6))  # 输出: 30

# 匿名函数可以在需要函数的任何地方使用，例如作为参数传递给其他函数
data = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, data) #将data中的每个元素都传入lambda函数中，返回一个新的列表
print(list(squared))  # 输出: [1, 4, 9, 16, 25]

# 过滤出偶数
evens = filter(lambda x: x % 2 == 0, data)
print(list(evens))  # 输出: [2, 4]

    