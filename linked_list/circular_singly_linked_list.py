class Node:

	def __init__(self, value):
		self.value = value
		self.next = None


class CircularSinglyLinkedList:

	def __init__(self):
		self.head = None
		self.tail = None


	def insert(self, value, location):
		node = Node(value)

		if self.head is None:
			self.head = self.tail = node.next = node

		elif location == 0:
			node.next = self.head.next
			self.head = node
			self.tail.next = node

		elif location == -1:
			node.next = self.head
			self.tail.next = node
			self.tail = node

		else:
			temp_node = self.head
			index = 0
			while index < location-1:
				if temp_node.next == self.head:
					break
				temp_node = temp_node.next
				index += 1
			if temp_node.next == self.head:
				node.next = self.head
				self.tail.next = node
				self.tail = node
			else:
				node.next = temp_node.next
				temp_node.next = node

	def delete(self, location):
		if self.head is None:
			print("There are no nodes")
		elif self.head == self.tail:
			self.head = self.tail = None
		elif location == 0:
			self.head = self.head.next
			self.tail.next = self.head
		elif location == -1:
			node = self.head
			while True:
				if node.next.next == self.head:
					self.tail = node
					node.next = self.head
					break
				node = node.next
		else:
			node = self.head
			index = 0
			while index < location-1:
				if node.next.next == self.head:
					break
				node = node.next
				index += 1
			node.next = node.next.next
			if node.next == self.head:
				self.tail = node

	def clear(self):
		self.head = self.tail = self.tail.next = None


	def __iter__(self):
		node = self.head
		while node:
			yield node
			if node.next == self.head:
				break
			node = node.next


linked_list = CircularSinglyLinkedList()
linked_list.insert(100,0)
linked_list.insert(1.5,2)
print([node.value for node in linked_list])
linked_list.clear()
print([node.value for node in linked_list])