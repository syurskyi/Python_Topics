'''
Created on Oct 29, 2017

@author: MT
'''
class Solution(object
    ___ numDistinctIslands2(self, grid
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        __ not grid or not grid[0]: r_ 0
        m, n = le.(grid), le.(grid[0])
        hashset = set()
        count = 0
        ___ i in range(m
            ___ j in range(n
                __ grid[i][j] __ 1:
                    res = [i, i, j, j]
                    grid[i][j] = 2
                    self.helper(grid, i, j, res)
                    keys = self.generateKeys(grid, res)
                    found = False
                    ___ key in keys:
                        __ key in hashset:
                            found = True
                            break
                    __ not found:
                        hashset.add(keys.pop())
                        count += 1
        r_ count
    
    ___ helper(self, grid, i, j, res
        res[0] = min(res[0], i)
        res[1] = max(res[1], i)
        res[2] = min(res[2], j)
        res[3] = max(res[3], j)
        m, n = le.(grid), le.(grid[0])
        ___ x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1
            __ 0 <= x < m and 0 <= y < n and grid[x][y] __ 1:
                grid[x][y] = 2
                self.helper(grid, x, y, res)
    
    ___ generateKeys(self, grid, res
        hashset = set()
        up, down, left, right = res[0], res[1], res[2], res[3]
        subGrid = []
        ___ i in range(up, down+1
            tmp = []
            ___ j in range(left, right+1
                tmp.append(grid[i][j])
            subGrid.append(tmp)
        self.addRotationKeys(subGrid, hashset)
        r_ hashset
    
    ___ addRotationKeys(self, grid, hashset
        grid1 = grid
        grid2 = grid[::-1]
        grid3 = [row[::-1] ___ row in grid]
        ___ grid in [grid1, grid2, grid3]:
            grid0 = grid
            ___ _ in range(4
                m, n = le.(grid0), le.(grid0[0])
                newGrid = [[0]*m ___ _ in range(n)]
                ___ i in range(m
                    ___ j in range(n
                        newGrid[j][i] = grid0[i][j]
                hashset.add(self.getKey(newGrid))
                grid0 = newGrid
            ___ _ in range(4
                m, n = le.(grid0), le.(grid0[0])
                newGrid = [[0]*m ___ _ in range(n)]
                ___ i in range(m
                    ___ j in range(n
                        newGrid[n-1-j][m-1-i] = grid0[i][j]
                hashset.add(self.getKey(newGrid))
                grid0 = newGrid
    
    ___ getKey(self, grid
        r_ ','.join([''.join([str(num) ___ num in row]) ___ row in grid])
    
    ___ test(self
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
        ___ grid in testCases:
            print('grid:')
            grid = [[int(c) ___ c in row] ___ row in grid]
            print('\n'.join([str(row) ___ row in grid]))
            result = self.numDistinctIslands2(grid)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
