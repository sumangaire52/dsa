import queue as q

queue = q.Queue(maxsize=3)

queue.put(1)
queue.put(2)
queue.put(3)
print(queue.full())
print(queue.get())
print(queue.full())
print(queue.qsize())