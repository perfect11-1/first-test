def f1(x):
    return x**2
date1 = [1,2,3,4,5,6,7,8,9]
date2 = map(f1,date1) #将date1中的每个元素都传入f1函数中，返回一个新的列表
print(list(date2))