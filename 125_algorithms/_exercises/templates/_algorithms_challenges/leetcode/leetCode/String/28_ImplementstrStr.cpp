/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-06 21:22:30
 */

c.. Solution {
public:
    int strStr(string haystack, string needle) {
        __(needle__"")  r_ 0;
        int str_len = haystack.size();
        int pat_len = needle.size();
        ___(int i=0;i<str_len-pat_len+1;i++){
            int j=0;
            ___(;j<pat_len;j++){
                __(haystack[i+j] != needle[j]){
                    ______;
                }
            }
            __(j __ pat_len){
                r_ i;
            }
        }
        r_ -1;
    }
};

/*
""
""
"abaa"
"aa"
"aaabbb"
"abbb"
*/
