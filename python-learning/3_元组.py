#创建空元组
tuple1 = ()
print(tuple1)

#当元祖中只有个一个值时，需要在值后面添加一个逗号
tuple2 = (1,)
print(tuple2)

#元组的元素不能被修改
# tuple2[0] = 2  # 会报错
# print(tuple2)

tuple3 = (1,2,3,4,5,6,7,8)
#元组的元素可以被访问
print(tuple3[0])

#元组的元素可以被切片
print(tuple3[0:3])
#元组的元素可以被遍历
for i in tuple3:
    print(i)
