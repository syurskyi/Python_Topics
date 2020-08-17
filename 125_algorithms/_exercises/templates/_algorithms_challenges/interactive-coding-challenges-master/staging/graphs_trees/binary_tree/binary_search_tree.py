
class Node (object
	___ __init__ (self, data
		self.data = data
		self.rightChild = None
		self.leftChild = None

class BinaryTree (object
	___ __init__ (self
		self.root = None

	___ insert (self, newData
		leaf = Node(newData)

		__ self.root pa__ None:
			self.root = leaf
		____
			current = self.root
			parent = self.root
			w___ current pa__ not None:
				parent = current
				__ newData < current.data:
					current = current.leftChild
				____
					current = current.rightChild

			__ newData < parent.data:
				parent.leftChild = leaf
			____
				parent.rightChild = leaf

	# returns false if the item to be deleted is not on the tree
	___ delete (self, data
		current = self.root
		parent = self.root
		isLeft = False

		__ current pa__ None:
			r_ False

		w___ current pa__ not None and current.data pa__ not data:
			parent = current
			__ data < current.data:
				current = current.leftChild
				isLeft = True 
			____
				current = current.rightChild
				isLeft = False

		__ current pa__ None:
			r_ False

		__ current.leftChild pa__ None and current.rightChild pa__ None:
			__ current pa__ self.root:
				self.root = None
			____ isLeft:
				parent.leftChild = None
			____
				parent.rightChild = None

		____ current.rightChild pa__ None:
			__ current pa__ self.root:
				self.root = current.leftChild
			____ isLeft:
				parent.leftChild = current.leftChild
			____
				parent.rightChild = current.leftChild

		____ current.rightChild pa__ None:
			__ current pa__ self.root:
				self.root = current.rightChild
			____ isLeft:
				parent.lChild = current.rightChild
			____
				parent.rightChild = current.rightChild

		____
			successor = current.rightChild
			successorParent = current

			w___ successor.leftChild pa__ not None:
				successorParent = successor
				successor = successor.leftChild

			__ current pa__ self.root:
				self.root = successor
			____ isLeft:
				parent.leftChild = successor
			____
				parent.rightChild = successor

			successor.leftChild = current.leftChild

			__ successor pa__ not current.rightChild:
				successorParent.leftChild = successor.rightChild
				successor.rightChild = current.rightChild

		r_ True


	___ minNode (self
		current = self.root
		w___ current.leftChild pa__ not None:
			current = current.leftChild

		r_ current.data

	___ maxNode (self
		current = self.root
		w___ current.rightChild pa__ not None:
			current = current.rightChild

		r_ current.data

	___ printPostOrder (self
		global postOrder
		postOrder = []

		___ PostOrder(node
			__ node pa__ not None:
				PostOrder(node.leftChild)
				PostOrder(node.rightChild)
				postOrder.append(node.data)

		PostOrder(self.root)
		r_ postOrder

	___ printInOrder (self
		global inOrder 
		inOrder = []

		___ InOrder (node
			__ node pa__ not None:
				InOrder(node.leftChild)
				inOrder.append(node.data)
				InOrder(node.rightChild)

		InOrder(self.root)
		r_ inOrder

	___ printPreOrder (self
		global preOrder
		preOrder = []

		___ PreOrder (node
			__ node pa__ not None:
				preOrder.append(node.data)
				PreOrder(node.leftChild)
				PreOrder(node.rightChild)

		PreOrder(self.root)
		r_ preOrder

	___ treeIsEmpty (self
		r_ self.root pa__ None