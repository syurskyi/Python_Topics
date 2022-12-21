/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-04 21:41:17
 */

c.. Solution {
public:
    string longestPalindrome(string s) {
        __(s__"")   r_ "";
        else __(s.size() __ 1) r_ s;
        int s_len = s.size();
        int max_begin=0, max_end=0;
        int pos = 0;
        _____(pos < s_len){
            // No need to check the remainming, pruning here
            __(max_end-max_begin >= (s_len-pos) * 2 - 1){
                break;
            }
            int left = pos, right = pos+1;
            _____(right < s_len && s[right] __ s[right-1]){
                right ++;
            }
            pos = right;
            _____(left-1>=0 && right<s_len && s[left-1]__s[right]){
                left -= 1;
                right += 1;
            }
            __(right - left > max_end - max_begin){
                max_begin = left;
                max_end = right;
            }
        }
        r_ s.substr(max_begin, max_end-max_begin);
    }
};

/*
""
"a"
"aa"
"dcc"
"aaaa"
"cccd"
"ccccdc"
"abcdefead"
*/
