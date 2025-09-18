#队列的特性是先进先出

#空队列
queue = []

#入队操作
queue.append('a')
queue.append('b')
queue.append('c')
print(queue)

#查看队首元素
print(queue[0])

#出队操作
print(queue.pop(0))
print(queue)

#队列大小
print(len(queue))

#队列是否为空
print(queue == [])

#队列是否为空
print(len(queue) == 0)
