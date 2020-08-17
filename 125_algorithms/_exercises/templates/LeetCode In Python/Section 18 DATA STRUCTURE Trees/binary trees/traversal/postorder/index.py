

c_ Node:
    ___  -  value
        .left _ N..
        .right _ N..
        .data _ value


___ postorder(node
    __(node pa__ no. N..
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
