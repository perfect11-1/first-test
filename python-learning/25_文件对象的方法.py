import pickle

with open('demo01.txt', 'r', encoding='utf-8') as f:
    #print(f.read()) # 读取文件所有内容
    #print(f.readline()) # 读取文件的一行内容
    list1 = f.readlines() # 读取文件所有内容，返回一个列表，每个元素为文件的一行内容
    print(type(list1))
    print(list1)
    print(len(list1))
    print(f.tell())   # 打印光标当前位置，单位为字节


