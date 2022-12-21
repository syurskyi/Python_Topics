/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-06-26 20:16:28
 */
c.. Solution {
public:
    double myPow(double x, int n) {
        // Simple recursively way.
        __(n __ 0){
            r_ 1.0;
        }

        int half_abs = abs(n/2);
        __(n>0){
            double result = myPow(x*x, half_abs);
            __(n&0x1 __ 1){
                result *= x;
            }
            r_ result;
        }
        else{
            double result = 1/myPow(x*x, half_abs);
            __(n&0x1 __ 1){
                result *= 1/x;
            }
            r_ result;
        }
    }
};

c.. Solution_2{
public:
    double myPow(double x, int n) {
        /* Another way: shorter code.
         * According to: https://leetcode.com/problems/powx-n/
         * Important here.  Or if n == INT_MIN, it will overload.
         */
        long ln = n;
        __(ln__0){
            r_ 1.0;
        }
        __(ln<0){
            ln = -ln;
            x = 1/x;
        }
        r_ ln&0x1__1 ? x * myPow(x*x, ln/2) : myPow(x*x, ln/2);
    }
};

/*
8.88023
3
2.00000
-2147483648
2.2
-100
*/
