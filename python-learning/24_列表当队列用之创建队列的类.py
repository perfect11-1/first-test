#队列的特性是先进先出
class Queue:
    def __init__(self):
        # 初始化空列表作为队列存储
        self.items = []
    
    def enqueue(self, item):
        # 入队操作
        self.items.append(item)
    
    def dequeue(self):
        # 出队操作
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError('dequeue from empty queue')
    def peek(self):
        # 查看队首元素
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError('peek from empty queue')
    
    def is_empty(self):
        # 判断队列是否为空
        return len(self.items) == 0
    
    def size(self):
        # 返回队列大小
        return len(self.items)

queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')
print(queue.items)

print("队首的元素是： ", queue.peek())

# 出队操作
print("出队的元素是： ", queue.dequeue())
print(queue.items)
print("队列的大小是： ", queue.size())
print("队列是否为空： ", queue.is_empty())


