#栈的特性是先进后出
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from empty stack')
    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            raise IndexError('peek from empty stack')
    def is_empty(self):
        return self.stack == []
    def size(self):
        return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.stack)
print("栈顶元素： ", stack.peek())
print("栈的大小： ", stack.size())
print("弹出的栈顶元素： ", stack.pop())
print(stack.stack)
print("栈是否为空： ", stack.is_empty())
print("栈的大小： ", stack.size())

