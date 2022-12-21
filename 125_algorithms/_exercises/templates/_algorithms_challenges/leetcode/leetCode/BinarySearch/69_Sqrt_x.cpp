/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-01 20:42:32
 */

c.. Solution {
public:
    int mySqrt(int x) {
        __(x < 2){
            r_ x;
        }
        int low = 0, high = x;
        _____(low <= high){
            int mid = low + (high - low) / 2;
            // mid * mid will overflow when mid > sqrt(INT_MAX)
            __(x / mid >= mid  && x / (mid+1) < (mid+1)){
                r_ mid;
            }
            else __(x / mid < mid){
                high = mid - 1;
            }
            else{
                low = mid + 1;
            }
        }
        r_ -1; // Can'e be reached!
    }
};

c.. Solution_2{
public:
    int mySqrt(int x) {
        // Newton iterative method
        long ans = x;
        _____(ans * ans > x){
            ans = (ans + x/ans) / 2;
        }
        r_ ans;
    }
};

/*
0
1
15
90
1010
*/
