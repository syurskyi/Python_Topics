/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-15 22:44:13
 */


c.. Solution {
public:
    int nthUglyNumber(int n) {
        __(n<=0){
            r_ -1;
        }
        vector<int> uglys(n, 1);
        int p_2=0, p_3=0, p_5=0;
        ___(int i=1; i<n; i++){
            int v_2 = uglys[p_2] * 2;
            int v_3 = uglys[p_3] * 3;
            int v_5 = uglys[p_5] * 5;
            uglys[i] = min(v_2, min(v_3, v_5));

            // Update the p_2, p_3, p_5;
            __(uglys[i] __ v_2)     p_2++;
            __(uglys[i] __ v_3)     p_3++;
            __(uglys[i] __ v_5)     p_5++;
        }
        r_ uglys[n-1];
    }
};

/*
-9
0
1
160
*/
