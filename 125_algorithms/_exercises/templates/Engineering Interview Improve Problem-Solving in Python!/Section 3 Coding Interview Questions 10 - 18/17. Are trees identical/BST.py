class Node:
    val  0
    left  0
    right  0
    def __init__(self, val):
        self.val  val

class BST:
    
    def __init__(self, val):
        self.root  Node(val)

    def insert(self, val, node):
        __ node.val < val:
            __ node.right:
                #go right
                self.insert(val, node.right)
            else:
                node.right  Node(val) #insert
        elif val < node.val:
            __ node.left:
                #go left
                self.insert(val, node.left)
            else:
                node.left  Node(val)
        else:
            print(val, " Already in tree")

    def number_of_leaves(self, node):
        __ node.left and node.right:
            return self.number_of_leaves(node.left) + self.number_of_leaves(node.right)
        elif node.left:
            return self.number_of_leaves(node.left)
        elif node.right:
            return self.number_of_leaves(node.right)
        else:
            #leave
            return 1
    
    def number_of_leaves_i(self):
        leaves  0
        nodes  [self.root]
        w___ nodes:
            node  nodes[0]
            __ node.left:
                nodes.append(node.left)
            __ node.right:
                nodes.append(node.right)
            __ (not node.left) and (not node.right):
                leaves + 1
            del nodes[0]
        return leaves

    def height(self, node):
        __ node.left and node.right:
            print(node.val, " Height of left ", self.height(node.left)," Hegiht of right ", self.height(node.right))
            return 1 + max(self.height(node.left), self.height(node.right))
        elif node.left:
            #print(node.val, self.height(node.left))
            return 1 + self.height(node.left)
        elif node.right:
            #print(node.val, self.height(node.right))
            return 1 + self.height(node.right)
        else:
            #print(node.val)
            return 1

    def is_identical(self, second_root):
        nodes1  [self.root]
        nodes2  [second_root]
        w___ nodes1 and nodes2:
            node  nodes1[0]
            node2  nodes2[0]
            __ node.val __ node2.val:
                __ node.left:
                    nodes1.append(node.left)
                __ node.right:
                    nodes1.append(node.right)
                __ node2.left:
                    nodes2.append(node2.left)
                __ node2.right:
                    nodes2.append(node2.right)
            else:
                return F..
            del nodes1[0]
            del nodes2[0]
        return len(nodes1) __ len(nodes2)