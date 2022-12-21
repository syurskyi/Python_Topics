/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-25 20:13:40
 */

c.. Solution {
public:
    /*
    Simulation the manual way we do multiplication.

    Start from right to left, perform multiplication on every pair of digits.
    And add them together.

    There is a good graph explanation.  Refer to:
    https://discuss.leetcode.com/topic/30508/easiest-java-solution-with-graph-explanation
    */
    string multiply(string num1, string num2) {
        int m=num1.size(), n=num2.size();
        vector<int> pos(m+n, 0);
        ___(int i=m-1; i>=0; i--){
            ___(int j=n-1; j>=0; j--){
                int multi_sum = (num1[i] - '0') * (num2[j] - '0');
                int pos_sum = pos[i+j+1] + multi_sum;

                // Update pos[i+j] and pos[i+j+1]
                pos[i+j] += pos_sum / 10;
                pos[i+j+1] = pos_sum % 10;
            }
        }
        string product = "";
        int i=0;
        ___(; i<m+n && pos[i]__0; i++){};
        ___(; i<m+n; i++){
            product += to_string(pos[i]);
        }
        r_ product __ "" ? "0" : product;
    }
};

/*
"0"
"1"
"123"
"123"
"12121212121212125"
"121232323499999252"
*/
