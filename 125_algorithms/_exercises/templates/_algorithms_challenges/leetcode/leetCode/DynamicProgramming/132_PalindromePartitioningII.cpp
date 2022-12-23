/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-10-11 10:06:28
 */

c.. Solution {
public:
    /*
    Dynamic Programming:
    cuts[i]: minimum cuts needed for a palindrome partitioning of s[i:], so we want cuts[0].

    To get cuts[i-1], we scan j from i-1 to len(s)-1.
    Once we comes to a is_palindrome[i-1][j]==true:
        if j==len(s)-1, the string s[i-1:] is a Pal, cuts[i-1] is 0;
        else: the current cut num (first cut s[i-1:j+1] and then cut the rest
        s[j+1:]) is 1+cuts[j+1], compare it to the exisiting cuts[i-1], repalce if smaller.

    is_palindrome[i][j]: whether s[i:j+1] is palindrome.
    Here we need not to compute the is_palindrome in advance.
    We use "Dynamic Programming" too, the formula is very intuitive:
    is_palindrome[i][j] = true if (is_palindrome[i+1][j-1] and s[i] == s[j]) else false

    A better O(n) space solution can be found here:
    https://discuss.leetcode.com/topic/2840/my-solution-does-not-need-a-table-for-palindrome-is-it-right-it-uses-only-o-n-space
    */

    int minCut(string s) {
        __(s__"")   r_ 0;
        int l.. = s.size();
        std::vector<int> cuts(l.., 0);
        // Initialize the cuts array.
        ___(int i=0; i<l..; i++){
            cuts[i] = l.. - i-1;
        }
        std::vector<std::vector<bool>> is_palindrome(l.., std::vector<bool>(l.., false));
        ___(int i=l..-1; i>=0; i--){
            ___(int j=i; j<l..; j++){
                __((j-i<=2 && s[i]__s[j]) || (s[i]__s[j] && is_palindrome[i+1][j-1])){
                    is_palindrome[i][j]=true;
                    __(j__len-1){
                        cuts[i]=0;
                    }
                    else{
                        cuts[i] = m.. cuts[i], cuts[j+1]+1);
                    }
                }
            }
        }
        r_ cuts[0];
    }
};

/*
""
"aab"
"aabb"
"aabaa"
"acbca"
"acbbca"
*/
