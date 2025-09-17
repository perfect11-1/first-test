employees = {
    '张三': '18',
    '李四': '20',
    '王五': '22'
}

#遍历字典的键
for key in employees:  
    print(key, employees[key])

#遍历字典的键值对
for key, value in employees.items():
    print(key, value)  

#遍历字典的键值对，同时获取索引
for index, (key, value) in enumerate(employees.items()):
    print(index, key, value)


print("下一个样例#####################################")

for i in range(0,10): #range()函数生成一个整数序列，默认从0开始，默认步长为1
    print(i)

print("下一个样例#####################################")

for i in range(0,10,2): #range()函数生成一个整数序列，默认从0开始，步长为2
    print(i,end='号 ')
