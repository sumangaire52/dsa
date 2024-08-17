class Node:

	def __init__(self, value=None):
		self.value = value
		self.next = None


class SinglyLinkedList:

	def __init__(self):
		self.head = None
		self.tail = None

	def insert(self, value, location):
		new_node = Node(value)

		# if head is None that means there are no nodes in the linked list
		# so we need to head the new node to the head
		if self.head is None:
			self.head = new_node
			self.tail = new_node

		# if location is 0, we need to assign the new node as head
		# and point the current head as next reference to the new node
		elif location == 0:
			new_node.next = self.head
			self.head = new_node

		# if location is last, we need to set current tail's next reference as new node
		# assign linked list's tail as new node
		elif location == -1:
			self.tail.next = new_node
			self.tail = new_node

		# if we need to insert in the middle of the linked list
		# find the current node at the given location
		# assign new node's next reference to the current node's next reference
		# assign current node's next reference to the new node
		else:
			temp_node = self.head
			index = 0
			while index < location-1:
				if temp_node.next:
					temp_node = temp_node.next
					index += 1
				else:
					break
			new_node.next = temp_node.next
			temp_node.next = new_node

	def delete(self, location):
		if self.head is None:
			print("List is empty")

		elif location == 0:
			if self.head == self.tail:
				self.head = self.tail = None
			else:
				self.head = self.head.next

		elif location == -1:
			if self.head == self.tail:
				self.head = self.tail = None
			else:
				temp_node = self.head
				while temp_node.next.next != None:
					temp_node = temp_node.next
				temp_node.next = None
				self.tail = temp_node

		else:
			temp_node = self.head
			index = 0
			while index < location-1:
				temp_node = temp_node.next
				index += 1
			temp_node.next = temp_node.next.next

	def clear(self):
		self.head = self.tail = None


	def __iter__(self):
		node = self.head
		while node:
			yield node
			node = node.next


linked_list = SinglyLinkedList()

# create 2 nodes
linked_list.insert(0,0)
linked_list.insert(0,0)
linked_list.insert(0,0)
print([node.value for node in linked_list])
linked_list.clear()
print([node.value for node in linked_list])