class Queue:

	def __init__(self, max_size):
		self.items = max_size * [None]
		self.max_size = max_size
		self.start = -1
		self.top = -1


	def is_full(self):
		if self.top == self.start-1:
			return True
		elif self.start == 0 and self.top == self.max_size-1:
			return True
		return False

	def is_empty(self):
		return self.top == -1

	def enqueue(self, value):
		if self.is_full():
			return "Queue is full"
		else:
			if self.top == self.max_size-1:
				self.top = 0
			else:
				self.top += 1
				if self.start == -1:
					self.start = 0
		self.items[self.top] = value

	def dequeue(self):
		if self.is_empty():
			return "Queue is empty"
		else:
			# this means queue has only one element
			element = self.items[self.start]
			start = self.start
			if self.start == self.top:
				self.start = -1
				self.top = -1
			elif self.start+1 = self.max_size:
				self.start = 0
			else:
				self.start += 1
			self.items[start] = None
			return element

	def peek(self):
		if self.is_empty():
			return "List is empty"
		return self.items[self.start]

	def delete(self):
		self.items = self.max_size * [None]
		self.start = self.top = -1

	def __str__(self):
		return f"{self.items}"


queue = Queue(2)
queue.enqueue(1)
queue.enqueue(2)
print(queue.enqueue(100))
print(queue)
print(queue.is_full())