class Node:

	def __init__(self, value=None):
		self.value = value
		self.next = None
		self.prev = None


class CircularDoublyLinkedList:

	def __init__(self):
		self.head = None
		self.tail = None

	def __iter__(self):
		node = self.head
		while node:
			yield node
			if node.next == self.head:
				break
			node = node.next

	def create(self, value):
		node = Node(value)
		self.head = self.tail = node.next = node.prev = node

	def insert(self, value, location):
		if self.head is None:
			self.create(value)
		node = Node(value)
		if location == 0:
			node.next = self.head
			node.prev = self.tail
			self.head.prev = node
			self.tail.next = node
			self.head = node
		elif location == -1:
			node.next = self.head
			node.prev = self.tail
			self.tail.next = node
			self.head.prev = node
			self.tail = node
		else:
			temp_node = self.head
			index = 0
			while index < location-1:
				if temp_node.next == self.head:
					self.tail = node
					break
				temp_node = temp_node.next
				index += 1
			node.next = temp_node.next
			node.prev = temp_node
			temp_node.next.prev = node
			temp_node.next = node

	def reverse(self):
		value = []
		node = self.tail
		while True:
			value.append(node.value)
			node = node.prev
			if node == self.tail:
				break
		return value




linked_list = CircularDoublyLinkedList()
linked_list.create(10)
linked_list.insert(15,0)
linked_list.insert(16,0)
linked_list.insert(1.5, 15)						# [16,15,10,1.5]
# print([node.value for node in linked_list]) 	
linked_list.insert(18,-1)						# [16, 15, 10, 1.5, 18]
linked_list.insert(2,1)							# [16, 2, 15, 10, 18]
print([node.value for node in linked_list])
print(linked_list.reverse())