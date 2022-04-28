c_ Solution o..
    # def floodFill(self, image, sr, sc, newColor):
    #     """
    #     :type image: List[List[int]]
    #     :type sr: int
    #     :type sc: int
    #     :type newColor: int
    #     :rtype: List[List[int]]
    #     """
    #     r_ls, c_ls = len(image), len(image[0])
    #     color = image[sr][sc]
    #     if color == newColor:
    #         return image

    #     def dfs(r, c):
    #         if image[r][c] == color:
    #             image[r][c] = newColor
    #             if r - 1 >= 0: dfs(r - 1, c)
    #             if r + 1 < r_ls: dfs(r + 1, c)
    #             if c - 1 >= 0: dfs(r, c - 1)
    #             if c + 1 < c_ls: dfs(r, c + 1)

    #     dfs(sr, sc)
    #     return image

    ___ floodFill  image, sr, sc, newColor):
        # BFS with queue
        r_ls, c_ls = l.. image), l.. image[0])
        color = image[sr][sc]
        __ color __ newColor:
            r_ image
        queue = [(sr, sc)]
        w.. l.. queue) > 0:
            r, c = queue.pop(0)
            __ image[r][c] __ color:
                image[r][c] = newColor
                __ r - 1 >= 0: queue.append((r - 1, c))
                __ r + 1 < r_ls: queue.append((r + 1, c))
                __ c - 1 >= 0: queue.append((r, c - 1))
                __ c + 1 < c_ls: queue.append((r, c + 1))
        r_ image
