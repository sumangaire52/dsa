class Node:

	def __init__(self, value):
		self.value = value
		self.next = None


class LinkedList:

	def __init__(self):
		self.head = None

	def __iter__(self):
		node = self.head
		while node:
			yield node
			node = node.next

class Stack:

	def __init__(self):
		self.list = LinkedList()

	def is_empty(self):
		return self.list.head is None

	def push(self, value):
		node = Node(value)
		node.next = self.list.head
		self.list.head = node

	def peek(self):
		return self.list.head.value

	def pop(self):
		if self.is_empty():
			return "Stack is empty"
		else:
			value = self.list.head.value
			self.list.head = self.list.head.next
			return value

	def __str__(self):
		return " <- ".join([str(node.value) for node in self.list])


stack = Stack()
stack.push(10)
stack.push(15)
stack.push('x')
print(stack)
# print(stack.peek())
# print(stack.is_empty())
# print(stack)
print(stack.pop())
print(stack)