class Node:

	def __init__(self, value):
		self.value = value
		self.next = None


class LinkedList:

	def __init__(self):
		self.head = None
		self.tail = None

	def __iter__(self):
		node = self.head
		while node:
			yield node
			node = node.next


class Queueu:

	def __init__(self):
		self.items = LinkedList()


	def __str__(self):
		return " ".join([str(node.value) for node in self.items])


	def is_empty(self):
		return self.items.head == None


	def enqueu(self, value):
		node = Node(value)
		if self.is_empty():
			self.items.tail = node
			self.items.head = node
		else:
			self.items.tail.next = node
			self.items.tail = node


	def dequeu(self):
		if self.is_empty():
			return "Queueu is empty"
		else:
			temp_node = self.items.head
			if self.items.head == self.items.tail:
				self.items.head = self.items.tail = None
			else:
				self.items.head = self.items.head.next
			return temp_node.value

	def peek(self):
		if self.is_empty():
			return "Queueu is empty"
		return self.items.head.value

	def delete(self):
		self.items.head = self.items.tail = None

q = Queueu()
q.enqueu(5)
q.enqueu(6)
print(q.dequeu())
print(q.is_empty())
print(q)
print(q.peek())