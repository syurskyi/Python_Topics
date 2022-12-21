/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-06-30 16:15:49
 */

c.. Solution {
public:
    string addBinary(string a, string b) {
        string result = "";
        int c = 0, i = a.size() - 1, j = b.size() - 1;
        _____(i>=0 || j>=0 || c__1){
            c += i >= 0 ? a[i --] - '0' : 0;
            c += j >= 0 ? b[j --] - '0' : 0;
            result = char(c % 2 + '0') + result;
            c /= 2;
        }
        r_ result;
    }
};


c.. Solution_2 {
public:
    string addBinary(string a, string b) {
        __(a.size()__0){
            r_ b;
        }
        __(b.size()__0){
            r_ a;
        }
        __(a[a.size()-1] __ '1' && b[b.size()-1] __ '1'){
            r_ addBinary(addBinary(
                string(a.begin(), a.end()-1), string(b.begin(), b.end()-1)), "1") + "0";
        }
        __(a[a.size()-1] __ '0' && b[b.size()-1] __ '0'){
            r_ addBinary(string(a.begin(), a.end()-1), string(b.begin(), b.end()-1)) + "0";
        }
        else{
            r_ addBinary(string(a.begin(), a.end()-1), string(b.begin(), b.end()-1)) + "1";
        }
    }
};

/*
"0"
"0"
"111000"
"111111111"
*/
