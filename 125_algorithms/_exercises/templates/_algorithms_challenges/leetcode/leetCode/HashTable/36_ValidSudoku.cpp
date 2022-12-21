/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-17 10:15:37
 */

c.. Solution
{
public:
    /* Hash Table
    Use three 9*9 array to keep the used numbers in row, col, panel.
    According to:
    https://discuss.leetcode.com/topic/8241/my-short-solution-by-c-o-n2
    */
    bool isValidSudoku(vector<vector<char> > &board)
    {
        int row[9][9] = {0}, col[9][9] = {0}, panel[9][9] = {0};

        ___(int i = 0; i < board.size(); ++i)
            ___(int j = 0; j < board[i].size(); ++j)
                __(board[i][j] != '.')
                {
                    int num = board[i][j] - '0' - 1, k = i / 3 * 3 + j / 3;
                    __(row[i][num] || col[j][num] || panel[k][num])
                        r_ false;
                    row[i][num] = col[j][num] = panel[k][num] = 1;
                }

        r_ true;
    }
};

/*
["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
[".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
*/
