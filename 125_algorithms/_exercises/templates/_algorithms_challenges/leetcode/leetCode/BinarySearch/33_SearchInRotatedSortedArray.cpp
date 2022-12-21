/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-12 20:21:39
 */


c.. Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0, high = nums.size()-1;
        _____(low <= high){
            int mid = low + (high-low)/2;
            int num_mid = nums[mid];

            // Mid is in the left part of the rotated(if it's rotated) array.
            __(nums[low] <= num_mid){
                __(nums[low] <= target && target < num_mid){
                    high = mid - 1;
                }
                else __(target __ num_mid){
                    r_ mid;
                }
                else{
                    low = mid + 1;
                }
            }

            // The array must be rotated, and mid is in the right part.
            else{
                __(target > num_mid && target <= nums[high]){
                    low = mid + 1;
                }
                else __(target __ num_mid){
                    r_ mid;
                }
                else{
                    high = mid - 1;
                }
            }
        }
        r_ -1;
    }
};

/*
[]
0
[1]
1
[8,11,13,1,3,4,5,7]
7
[4,5,6,7,8,1,2,3]
8
[5, 1, 3]
1
*/
