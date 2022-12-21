/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-28 13:58:30
 */

c.. Solution {
public:
    int countDigitOne(int n)
    {
        __(n<=0) r_ 0;
        long long count = 1;
        _____(n){
            __(n<10){
                ______;
            }
            int digit = n % 10;
            n /= 10;
            count += n;
            __(digit __ 0)  count -= 1;
            count += countDigitOne(n-1) * 10;

            // 最后一行中数组1出现的次数
            _____(n){
                __(n%10__1) count += digit+1;
                n /= 10;
            }
        }
        r_ count;
    }
};

/*
-1
6
12
234545
*/
