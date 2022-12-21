"""
包括生成树，二叉搜索树的前后中遍历。

二叉搜索树在比较优质的情况下搜索和插入时间都是 O(logn) 的。在极端情况下会退化为链表 O(n)。
将无序的链表塞进二叉搜索树里，按左根右中序遍历出来就是排序好的有序链表。


"""

# 生成树操作。

c.. TreeNode o..

    ___ __init__(self , val, left=None, right=None

        self.val = val
        self.left = left
        self.right = right


c.. binarySearchTree o..
    """
        二叉搜索树，
        它的性质是左边节点都小于根节点，右边的都大于根节点。
        而且一般来说它是不存在重复元素的。

    """

    ___ __init__  root
        __ isinstance(root, TreeNode
            print(1)
            self.root = root
        ____
            self.root = TreeNode(root)

    ___ add  value
        # 从顶点开始遍历，找寻其合适的位置。
        root = self.root
        _____ 1:
            __ root.val < value:
                __ root.right is None:
                    __ self.search(value
                        ______
                    root.right = TreeNode(value)
                    ______
                ____
                    root = root.right
                    c_

            __ root.val > value:
                __ root.left is None:
                    __ self.search(value
                        ______
                    root.left = TreeNode(value)
                    ______
                ____
                    root = root.left
                    c_

            __ root.val __ value:
                ______

    ___ search  value
        # 查找一个值是否存在于这颗树中。
        r_ self._search(self.root, value)

    ___ _search  root, value
        __ root.val __ value:
            r_ True

        __ root.right:
            __ root.val < value:
                r_ self._search(root.right, value)

        __ root.left:
            __ root.val > value:
                r_ self._search(root.left, value)

        r_ False

    ___ delete(self
        pass

    ___ prevPrint(self
        # 根左右
        nodes = [self.root]
        result   # list
        _____ 1:
            __ n.. nodes:
                r_ result
            node = nodes.pop()
            result.append(node.val)

            __ node.right:
                nodes.append(node.right)

            __ node.left:
                nodes.append(node.left)

    ___ _middlePrint  root, result
        __ root.left:
            self._middlePrint(root.left, result)

        result.append(root.val)

        __ root.right:
            self._middlePrint(root.right,result)

    ___ middlePrint(self
        # 左根右
        result   # list
        self._middlePrint(self.root, result)

        r_ result

    ___ _suffPrint  root, result
        __ root.left:
            self._suffPrint(root.left, result)

        __ root.right:
            self._suffPrint(root.right,result)
        
        result.append(root.val)

    ___ suffPrint(self
        # 左右根
        result   # list
        self._suffPrint(self.root, result)

        r_ result


oneTree = binarySearchTree(5)

___ i __ r..(-5, 10
    oneTree.add(i)

print(oneTree.middlePrint())
print(oneTree.suffPrint())






