'''
Created on Oct 29, 2017

@author: MT
'''
c_ Solution(object):
    ___ numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        __ n.. grid o. n.. grid[0]: r.. 0
        m, n = l..(grid), l..(grid[0])
        hashset = set()
        count = 0
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ grid[i][j] __ 1:
                    res = [i, i, j, j]
                    grid[i][j] = 2
                    helper(grid, i, j, res)
                    keys = generateKeys(grid, res)
                    found = F..
                    ___ key __ keys:
                        __ key __ hashset:
                            found = T..
                            break
                    __ n.. found:
                        hashset.add(keys.pop())
                        count += 1
        r.. count
    
    ___ helper(self, grid, i, j, res):
        res[0] = m..(res[0], i)
        res[1] = max(res[1], i)
        res[2] = m..(res[2], j)
        res[3] = max(res[3], j)
        m, n = l..(grid), l..(grid[0])
        ___ x, y __ (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            __ 0 <= x < m a.. 0 <= y < n a.. grid[x][y] __ 1:
                grid[x][y] = 2
                helper(grid, x, y, res)
    
    ___ generateKeys(self, grid, res):
        hashset = set()
        up, down, left, right = res[0], res[1], res[2], res[3]
        subGrid    # list
        ___ i __ r..(up, down+1):
            tmp    # list
            ___ j __ r..(left, right+1):
                tmp.a..(grid[i][j])
            subGrid.a..(tmp)
        addRotationKeys(subGrid, hashset)
        r.. hashset
    
    ___ addRotationKeys(self, grid, hashset):
        grid1 = grid
        grid2 = grid[::-1]
        grid3 = [row[::-1] ___ row __ grid]
        ___ grid __ [grid1, grid2, grid3]:
            grid0 = grid
            ___ _ __ r..(4):
                m, n = l..(grid0), l..(grid0[0])
                newGrid = [[0]*m ___ _ __ r..(n)]
                ___ i __ r..(m):
                    ___ j __ r..(n):
                        newGrid[j][i] = grid0[i][j]
                hashset.add(getKey(newGrid))
                grid0 = newGrid
            ___ _ __ r..(4):
                m, n = l..(grid0), l..(grid0[0])
                newGrid = [[0]*m ___ _ __ r..(n)]
                ___ i __ r..(m):
                    ___ j __ r..(n):
                        newGrid[n-1-j][m-1-i] = grid0[i][j]
                hashset.add(getKey(newGrid))
                grid0 = newGrid
    
    ___ getKey(self, grid):
        r.. ','.j..([''.j..([s..(num) ___ num __ row]) ___ row __ grid])
    
    ___ test
        testCases = [
            [
                '11000',
                '10000',
                '00001',
                '00011',
            ],
            [
                '11100',
                '10001',
                '01001',
                '01110',
            ],
            [
                '0000111',
                '1111111',
                '0000000',
                '0000111',
                '1111110',
                '0001000',
            ],
            [
                '011',
                '111',
                '000',
                '111',
                '110',
            ],
            [
                '0111110110111111',
                '0000011111011101',
                '1010000100011101',
                '1111101000010011',
                '0100111111001111',
                '0101001001110100',
                '0001111100100001',
                '0111011010000001',
                '1101000100110110',
                '1101110011010010',
                '1010100011000010',
                '0011101101111100',
                '1100011101011111',
                '0001110101000101',
                '0101101000001011',
                '1100100101000110',
                '1100110010010010',
                '0111001011101010',
                '0100011001010100',
                '0101101010111100',
                '0101001110010001',
                '1101101100010000',
                '1001010000111111',
                '0001110100111100',
                '0011110001111000',
                '0001111111010000',
                '1111010001000010',
                '0111101110100110',
                '0011000111101111',
                '1101000110110100',
                '1001000110000001',
                '1100011111100001',
                '1010001000101110',
                '1100110000100011',
                '0010011010100011',
                '0011111011011001',
                '1100100100111101',
                '1011110110110011',
                '1001010111100011',
                '0100000010011110',
                '0110000100000000',
                '0010000100111110',
                '0000100111110010',
                '0011101000001111',
                '1000110101000001',
                '0110010000011101',
                '0111010110001111',
                '0001001101110110',
                '0010001101010110',
                '1000000101000110',
            ],
        ]
        ___ grid __ testCases:
            print('grid:')
            grid = [[i..(c) ___ c __ row] ___ row __ grid]
            print('\n'.j..([s..(row) ___ row __ grid]))
            result = numDistinctIslands2(grid)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
