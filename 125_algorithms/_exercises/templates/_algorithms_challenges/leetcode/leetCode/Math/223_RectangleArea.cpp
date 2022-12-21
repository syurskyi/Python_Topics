/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-12 09:17:10
 */

c.. Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int left = m..(A, E);
        int bottom = m..(B, F);
        int right = min(C, G);
        int top = min(D, H);
        int size = (D-B) * (C-A) + (H-F) * (G-E);
        __(left < right && bottom < top){
            size -= (top-bottom) * (right-left);
        }
        r_ size;
    }
};

/*
-2
-2
2
2
-2
-2
2
2
0
0
0
0
-1
-1
1
1
*/
