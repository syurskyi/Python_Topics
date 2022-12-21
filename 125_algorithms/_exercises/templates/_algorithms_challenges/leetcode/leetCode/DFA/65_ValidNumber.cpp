/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-06-30 15:29:11
 */

c.. Solution {
public:
    bool isNumber(string s) {
        /*
        DFA.  Details can be found here:
        https://github.com/xuelangZF/LeetCode/blob/master/Images/65_ValidNumber.png
        https://github.com/xuelangZF/LeetCode/blob/master/Images/65_StateConvert.png
        */
        //delete the  prefix whitespace
        _____(s[0]__' ')  s.erase(0,1);
        //delete the suffix whitespace
        _____(s[s.size()-1]__' ') s.erase(s.size()-1, 1);
        __(s.size() __ 0){
            r_ false;
        }
        vector<vector<int>> DFA_states_convert = {
            {2, 1, 8, -1},
            {2, -1, 8, -1},
            {2, -1, 3, 5},
            {4, -1, -1, 5},
            {4, -1, -1, 5},
            {7, 6, -1, -1},
            {7, -1, -1, -1},
            {7, -1, -1, -1},
            {4, -1, -1, -1}
        };

        int state = 0;
        ___(char c : s){
            int num = input_num(c);
            __(num__-1){
                r_ false;
            }
            state = DFA_states_convert[state][num];
            __(state__-1){
                r_ false;
            }
        }
        __(state __ 2 || state __ 3 || state __ 4 || state __7){
            r_ true;
        }
        r_ false;
    }

private:
    int input_num(char c){
        __(c>='0' && c<='9'){
            r_ 0;
        }
        else __(c__'+' || c__'-'){
            r_ 1;
        }
        else __(c__'.'){
            r_ 2;
        }
        else __(c__'e'){
            r_ 3;
        }
        else{
            r_ -1;
        }
    }
};

/*
# True
"""
" .1"
"012"
"+12"
"-12"
"12e1"
"12e-1"
"12e+1"
"12e0"
"0e1"
"-1e1"
"1.2"
".2"
".1e1"
"+.2"
"1."
"      .1 "
"46.e3"
"""

# False
"""
""
".e1"
"+.e3"
"10e1.2"
"+-12"
"12e"
"e1"
"1e1e1"
"0xaf"
"      .1 2"
"."
"  ."
" -."
*/
