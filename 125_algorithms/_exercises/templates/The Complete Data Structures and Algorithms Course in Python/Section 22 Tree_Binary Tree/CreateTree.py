#   Created by Elshad Karimov on 05/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

c_ TreeNode:
    ___  -   data, children = []
        data = data
        children = children
    
    ___ __str__  level=0
        ret = "  " * level + str(data)  + "\n"
        ___ child __ children:
            ret += child.__str__(level + 1)
        r_ ret
    
    ___ addChild  TreeNode
        children.ap..(TreeNode)

tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
tree.addChild(cold)
tree.addChild(hot)
tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])
cola = TreeNode('Cola', [])
fanta = TreeNode('Fanta', [])
cold.addChild(cola)
cold.addChild(fanta)
hot.addChild(tea)
hot.addChild(coffee)
print(tree)