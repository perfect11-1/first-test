#集合和列表相比,存在两个特点：1.集合是无序的，2.集合中的元素是唯一的，不重复的，哪怕赋值时配置了重复的值，但实际上重复的值会被忽略
#创建空集合：
name5 = set()
name5.add('a')
print(name5)

# 创建两个集合
name = {1,2,1,1,2,3,4,5}  # 重复元素会被自动去除
name1 = {1,2,3,4,5,6,7,8}

# 将name转换为集合对象
name2 = set(name)

# 集合差集运算
name3 = name2 - name1  # 使用减号运算符
print(name3)
name10 = name2.difference(name1)  # 使用difference()方法
print(name10)

name3 = name1 - name2  # 使用减号运算符
print(name3)
name10 = name1.difference(name2)  # 使用difference()方法
print(name10)


# 集合交集运算
name4 = name2 & name1  # 使用&运算符
print(name4)
name9 = name2.intersection(name1)  # 使用intersection()方法
print(name9)

# 集合并集运算
name5 = name2 | name1  # 使用|运算符
print(name5)
name8 = name2.union(name1)  # 使用union()方法
print(name8)

# 集合对称差集运算（并集减去交集）
name6 = name2 ^ name1  # 使用^运算符
print(name6)
name11 = name2.symmetric_difference(name1)  # 使用symmetric_difference()方法
print(name11)

# 判断两个集合是否没有交集
name12 = name2.isdisjoint(name1)  # 返回布尔值
print(name12)

# 判断是否为子集
name13 = name2.issubset(name1)  # 判断name2是否是name1的子集
print(name13)

# 判断是否为超集
name14 = name2.issuperset(name1)  # 判断name2是否是name1的超集
print(name14)

