

c_ Node:
    ___ __init__(, value
        .left _ None
        .right _ None
        .data _ value


___ postorder(node
    __(node is not None
        postorder(node.left)
        postorder(node.right)
        print(node.data)


# create root
root _ Node(4)
''' following is the tree after above statement 
	    4 
	  /   \ 
	None  None
'''

root.left _ Node(5)
root.right _ Node(6)

''' 5 and 6 become left and right children of 1 
		           4 
		       /       \ 
		      5	        6 
	      /  \      /   \ 
      None None  None  None
'''


root.left.left _ Node(7)
'''
7 becomes left child of 5
		           4 
		       /       \ 
		      5	        6 
	      /  \      /   \ 
       7   None  None  None
      / \
  None   None

'''
postorder(root)

#              4
#          /       \
#         5         6
#       /  \      /   \
#      7   None  None  None
#     / \
# None   None
