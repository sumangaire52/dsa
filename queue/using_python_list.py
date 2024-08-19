class Queue:
	def __init__(self):
		self.items = list()

	def __str__(self):
		return " ".join([str(value) for value in self.items])

	def is_empty(self):
		return self.items == list()

	def enqueue(self, value):
		self.items.append(value)

	def dequeue(self):
		if self.is_empty():
			return "Queue is empty"
		return self.items.pop(0)

	def peek(self):
		if self.is_empty():
			return "Queue is empty"
		return self.items[0]

	def clear(self):
		self.items = list()