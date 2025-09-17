def f1(x):
    return x > 10
data1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
data2 = filter(f1,data1) #将data1中的每个元素都传入f1函数中，返回一个新的列表
print(list(data2))
