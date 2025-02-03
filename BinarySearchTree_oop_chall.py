
# Challenge #5  by : https://www.w3resource.com/python-exercises/oop/index.php



class Node:
	"""docstring for Node"""
	def __init__(self, root):
		self.root = root
		self.left = None
		self.right = None



class BinarySearch(Node):
	# def __init__(self, root):
	# 		super().__init__(root)

	def insert(self, value):
		if value < self.root:
			if self.left is None:
				self.left = BinarySearch(value)
			else:
				self.left.insert(value)
		else:
			if self.right is None:
				self.right = BinarySearch(value)
			else:
				self.right.insert(value)
	
	def search(self):
		if self.left:
			self.left.search()
		print(self.root)
		if self.right:
			self.right.search()
			


tree1 = BinarySearch(10)
tree1.insert(5)
tree1.insert(18)
tree1.insert(22)
tree1.insert(4)
tree1.insert(96)
tree1.insert(10003)
tree1.insert(700)
tree1.insert(500)
tree1.insert(431)
tree1.insert(31)
tree1.insert(1)
tree1.insert(659)
tree1.insert(90)
tree1.insert(91)
tree1.insert(92)

print(tree1.search())