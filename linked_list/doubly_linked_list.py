class Node:

	def __init__(self, value=None):
		self.value = value
		self.next = None
		self.prev = None


class DoublyLinkedList:

	def __init__(self):
		self.head = None
		self.tail = None

	def create(self, value):
		node = Node(value)
		self.head = self.tail = node

	def insert(self, value, location):
		node = Node(value)
		# check if the list is empty
		# if empty insert at first position
		if self.head is None:
			self.head = self.tail = node

		elif location == 0:
			self.head.prev = node
			node.next = self.head
			self.head = node


		elif location == -1:
			node.next = None
			node.prev = self.tail
			self.tail.next = node
			self.tail = node

		else:
			temp_node = self.head
			index = 0
			while index < location-1:
				if temp_node.next is None:
					break
				temp_node = temp_node.next
				index += 1

			# this means new node should be the last node
			if temp_node.next is None:
				self.tail = node
			temp_node.next = node
			node.prev = temp_node



	def __iter__(self):
		node = self.head
		while node:
			yield node
			node = node.next

linked_list = DoublyLinkedList()
linked_list.insert(5,0)			# [5]
linked_list.insert(10,100)		# [5,10]
linked_list.insert(8,50)		# [5,10,8]
linked_list.insert(50,0)		# [50,5,10,8]
linked_list.insert(80,-1)		# [50, 5, 10, 8, 80]
print(linked_list.head.value)
print(linked_list.tail.value)
print(linked_list.tail.prev.value)
print([node.value for node in linked_list])

node = linked_list.tail
while node:
	print(node.value)
	node = node.prev