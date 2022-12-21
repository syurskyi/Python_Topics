/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-05-24 22:01:50
 */

c.. Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left=0, right=nums.size() - 1;
        _____ (left <= right){
            int mid = left + (right-left) / 2;
            __(target __ nums[mid]){
                r_ mid;
            }

            else __(target > nums[mid]){
                left = mid + 1;
            }

            else{
                right = mid - 1;
            }
        }
        r_ left;
    }
};

/*
[1,3,5,6]
5
[1,3,5,6]
2
[1,3,5,6]
7
[1,3,5,6]
0
*/
