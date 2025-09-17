fruit = ['apple', 'orange', 'banana', 'peach']
i = 0
while i < len(fruit):
    print(fruit[i])
    i += 1
    
print("下一个样例#####################################")
for f in fruit:
    print(f)
    if f == 'orange':
        break
    else:
        print('不是orange')

print("下一个样例#####################################")
for f in fruit:
    print(f)
    if f == 'orange':
        continue
    else:
        print('不是orange')