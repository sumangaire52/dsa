class Stack:

	def __init__(self):
		self.list = []

	def __str__(self):
		return ','.join(reversed(self.list))


	def is_empty(self):
		return self.list == []

	def delete(self):
		self.list = []
		return

stack = Stack()
print(stack.is_empty())