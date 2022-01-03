c_ Node:
    val  0
    left  0
    right  0
    ___ - , val):
        val  val

c_ BST:
    
    ___ - , val):
        root  Node(val)

    ___ insert(self, val, node):
        __ node.val < val:
            __ node.right:
                #go right
                insert(val, node.right)
            ____:
                node.right  Node(val) #insert
        ____ val < node.val:
            __ node.left:
                #go left
                insert(val, node.left)
            ____:
                node.left  Node(val)
        ____:
            print(val, " Already in tree")

    ___ number_of_leaves(self, node):
        __ node.left a.. node.right:
            r.. number_of_leaves(node.left) + number_of_leaves(node.right)
        ____ node.left:
            r.. number_of_leaves(node.left)
        ____ node.right:
            r.. number_of_leaves(node.right)
        ____:
            #leave
            r.. 1
    
    ___ number_of_leaves_i
        leaves  0
        nodes  [root]
        w___ nodes:
            node  nodes[0]
            __ node.left:
                nodes.a..(node.left)
            __ node.right:
                nodes.a..(node.right)
            __ (n.. node.left) a.. (n.. node.right):
                leaves + 1
            del nodes[0]
        r.. leaves

    ___ height(self, node):
        __ node.left a.. node.right:
            print(node.val, " Height of left ", height(node.left)," Hegiht of right ", height(node.right))
            r.. 1 + max(height(node.left), height(node.right))
        ____ node.left:
            #print(node.val, self.height(node.left))
            r.. 1 + height(node.left)
        ____ node.right:
            #print(node.val, self.height(node.right))
            r.. 1 + height(node.right)
        ____:
            #print(node.val)
            r.. 1

    ___ is_identical(self, second_root):
        nodes1  [root]
        nodes2  [second_root]
        w___ nodes1 a.. nodes2:
            node  nodes1[0]
            node2  nodes2[0]
            __ node.val __ node2.val:
                __ node.left:
                    nodes1.a..(node.left)
                __ node.right:
                    nodes1.a..(node.right)
                __ node2.left:
                    nodes2.a..(node2.left)
                __ node2.right:
                    nodes2.a..(node2.right)
            ____:
                r.. F..
            del nodes1[0]
            del nodes2[0]
        r.. l..(nodes1) __ l..(nodes2)