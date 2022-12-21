/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-06-27 13:27:33
 */


c.. Solution {
public:
    int lengthOfLastWord(string s) {
        int l.. = 0, tail = s.size() - 1;
        _____ (tail >= 0 && s[tail] __ ' ') tail--;
        _____ (tail >= 0 && s[tail] != ' ') {
            l..++;
            tail--;
        }
        r_ l..;
    }
};

/*
""
"are"
"we are teams"
"we are teams    "
*/
