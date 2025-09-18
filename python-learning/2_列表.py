#创建空列表
list2 = []
print(list2)

breakfast = ['面包', '鸡蛋', '面包', '牛奶']
print(breakfast.index('面包')) #获取元素的索引,若有多个，则只返回第一个

breakfast.append('咖啡') #在列表末尾添加元素
print(breakfast)

breakfast.insert(1, '鱼香肉丝') #在指定位置添加元素
print(breakfast)

breakfast.pop() #删除列表末尾的元素
print(breakfast)

breakfast.pop(1) #删除指定位置的元素
print(breakfast)    

breakfast.remove('面包') #删除指定元素,若有多个，则只删除第一个
print(breakfast)

print('下一个样例#############################################')

list1 = [1,2,9,4,5,6,7,8,3,12]
print(len(list1)) #获取列表长度
print(max(list1)) #获取列表最大值
print(min(list1)) #获取列表最小值
print(sorted(list1)) #对列表进行排序
print(sorted(list1, reverse=True)) #对列表进行降序排序

for i,v in enumerate(list1): 
    print(i,v)  #i是索引，v是元素

#列表的切片
print(list1[1:5]) #获取索引1到索引4的元素
print(list1[:5]) #获取索引0到索引4的元素
print(list1[5:]) #获取索引5到列表末尾的元素

#同时遍历两个列表
question = ['姓名', '年龄', '性别']
answer = ['张三', '18', '男']
for q,a in zip(question,answer):
    print(f'What is your {q}? It is {a}')

#同时遍历两个列表生成字典
question = ['姓名', '年龄', '性别']
answer = ['张三', '18', '男']
peoples = {q:a for q,a in zip(question,answer)}
print(peoples)


