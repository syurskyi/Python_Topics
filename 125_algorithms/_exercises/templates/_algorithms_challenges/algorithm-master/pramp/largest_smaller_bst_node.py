___ largest_smaller_bst_node(root, target
    ans = -1

    __ not root:
        r_ ans

    w___ root:
        __ root.val < target:
            ans = root.val
            root = root.right
        ____
            root = root.left

    r_ ans
