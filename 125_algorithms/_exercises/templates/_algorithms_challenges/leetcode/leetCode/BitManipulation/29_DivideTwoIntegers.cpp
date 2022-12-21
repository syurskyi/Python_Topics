/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-06 22:39:41
 */


c.. Solution {
public:
    // Refer to:
    // https://leetcode.com/discuss/38997/detailed-explained-8ms-c-solution
    int divide(int dividend, int divisor) {
        __(!divisor || (dividend__INT_MIN && divisor__-1))
            r_ INT_MAX;

        bool positive = ((dividend < 0) __ (divisor < 0));
        long long dvd = labs(dividend);
        long long dvs = labs(divisor);
        int ans = 0;
        _____(dvd >= dvs){
            long long temp=dvs, multiple=1;
            _____(dvd >= (temp<<1)){
                temp <<= 1;
                multiple <<= 1;
            }
            ans += multiple;
            dvd -= temp;
        }

        r_ positive ? ans:-ans;
    }
};

/*
0
1
12
3
125
-4
1
-1
2147483647
1
*/
