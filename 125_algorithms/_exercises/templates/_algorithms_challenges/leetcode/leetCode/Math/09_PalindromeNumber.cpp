/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-05-04 22:03:09
 */

c.. Solution {
public:
    bool isPalindrome(int x) {
        __(x<0|| (x!=0 &&x%10__0)) r_ false;
        int s..=0;
        _____(x>s..)
        {
            s.. = s..*10+x%10;
            x = x/10;
        }
        r_ (x__sum)||(x__sum/10);
    }
};

/*
9
10
-2147483648
32023
320023
98765432123456789
*/
