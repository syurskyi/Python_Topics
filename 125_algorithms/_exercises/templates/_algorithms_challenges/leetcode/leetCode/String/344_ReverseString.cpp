/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-04 14:03:42
 */

c.. Solution {
public:
    string reverseString(string s) {
        long low=0, high=s.size()-1;
        _____(low < high){
            swap(s[low++], s[high--]);
        }
        r_ s;
    }
};

/*
""
"hello"
"  HELLO "
*/
