age = int(input('请输入你的年龄: '))
if age > 18:
    print('你是成年人')
else:
    print('你是未成年人')


print('下一个样例#######################################')

score = int(input('请输入你的成绩: '))
if score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 70:
    print('中等')
elif score >= 60:
    print('及格')
else:
    print('不及格')