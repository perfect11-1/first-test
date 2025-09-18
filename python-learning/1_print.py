# -*- coding: utf-8 -*-

import sys

#print基本用法
name =  '小红' 
print('hello world')   #打印hello world
print('%s hello world' % name)  #打印 小红 hello world
print('hello world %s' % name)  #打印 hello world 小红
print('hello world %s, i am %s' % (name, 'xiao ming'))  #打印 hello world 小红, i am xiao ming
print('hello world %s, i am %s, i am %d years old' % (name, 'xiao ming', 18))  
#打印 hello world 小红, i am xiao ming, i am 18 years old

#print高级用法
print('##################################################')
print('111', '222','333')  #打印111 222 333
print('111', '222','333', sep='')  #打印 111222333
print('111', '222','333', sep='&')  #打印 111&222&333
print('111', '222','333', sep='-', end='he')  #打印 111-222-333he
print('111', '222','333', sep='->', end='\n')  #打印 111->222->333

print("hello\nworld")  #将打印内容换行

print("hello world",file=open("demo01.txt","a"),end="\n\n")  #将打印内容写入文件，换两行
print("hello world",file=open("demo01.txt","a"))  #将打印内容写入文件

print("""aaa    #通过三引号打印多段文字
bbb
ccc
ddd""")

print(int(8.88))  #将浮点数转换为整数
print(float(8))  #将整数转换为浮点数
print(str(8))  #将整数转换为字符串

fruit = ['apple', 'orange', 'banana', 'peach']
#format方式连接字符串
print("我喜欢吃{2}, {0}, {1}, {3}这些水果".format(fruit[0],fruit[1],fruit[2],fruit[3])) 
print(f"我喜欢吃{fruit[0]}, {fruit[1]}, {fruit[2]}, {fruit[3]}这些水果") 



#生成平方立方表
"""
打印从1到9的数字及其平方和立方，格式化为对齐的表格。
输出格式为：数字（2位宽度）、平方（3位宽度）、立方（4位宽度）。
"""
for x in range(1,10):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

#另一种方式生成平方立方表
"""
使用repr()函数将数字转换为字符串，并使用rjust()方法右对齐输出，
确保数字在指定宽度内右对齐,其中rjust()方法的第一个参数为指定宽度。
"""
for x in range(1,10):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))

# 测试中文打印
print('测试中文打印能力')
# 获取当前文件编码
print('当前系统默认编码:', sys.getdefaultencoding())
# 获取当前终端编码
print('当前终端编码:', sys.stdout.encoding)

