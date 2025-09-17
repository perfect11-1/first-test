num1 = 10
def my_func():
    global num1   #全局变量
    num1  += 1
    print(num1)

my_func()
print(num1)


print('下一个样例#################################')
num1 = 10
def my_func():
    num1 = 100   #局部变量
    num1  += 1
    print(num1)

my_func()
print(num1)


print('下一个样例#################################')
def add(a, b):
    return a + b  #将函数的结果返回出来，用于函数外使用

sum_result = add(1, 2)
print(sum_result)