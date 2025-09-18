#字典实际就是两层列表，但是对两层列表操作太麻烦，所以字典应运而生
#字典的每个元素都是一个键值对，键值对之间用逗号隔开，每个键值对用冒号隔开
#字典的键必须是唯一的，值可以重复
#字典的键必须是不可变的，值可以是任意的
#创建空字典方式一
from turtle import home

#创建空字典方式一
name = {}
print(name)
#创建空字典方式二
emptydir = dict()
print(emptydir)

peoples = {
    'name': '张三',
    'age': 18,
    'sex': '男'
}
peoples['country'] = '中国' #添加键值对 
print(peoples)  

peoples['age'] = 20 #修改键值对
print(peoples)

sorted(peoples) #排序
print(sorted(peoples.keys()))  #等同于print(sorted(peoples))
print(sorted(peoples.items()))

del peoples['sex'] #删除键值对
print(peoples)

#获取字典中的值
print(peoples['name'])
#如果键不存在，会报错
print(peoples['country'])
#为了避免报错，我们可以使用get()方法
print(peoples.get('country'))

for k,v in peoples.items():
    print(k,v)


