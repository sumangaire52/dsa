from collections import deque

q = deque(maxlen=3)

# enqueue
q.append(1) 	# [1]
q.append(2)		# [1,2]
q.append(3)		# [1,2,3]
q.append(4)		# [2,3,4]
print(q)
# dequeue
q.popleft()
print(q)
q.clear()
print(q)