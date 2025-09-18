#栈的特性是先进后出
#空栈
stack = [] 

#压入操作
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)

#弹出操作
stack.pop()
print(stack.pop())
print(stack)

#查看栈的长度
print(len(stack))

#判断栈是否为空
print(len(stack) == 0)

#判断栈是否为空
print(stack == [])

#查看栈顶元素
print(stack[-1])