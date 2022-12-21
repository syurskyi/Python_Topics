/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-05-24 21:39:59
 */

c.. Solution {
public:
    int findFirstAppear(const vector<int> &nums, int target){
        int left = 0, right = nums.size()-1;
        _____(left <= right){
            int mid = left + (right - left) / 2;
            __ (target __ nums[mid] && mid - 1 >= left && target __ nums[mid - 1]){
                right = mid - 1;
            }
            else __(target __ nums[mid]){
                r_ mid;
            }
            else __(target > nums[mid]){
                left = mid + 1;
            }
            else{
                right = mid - 1;
            }
        }
        r_ -1;
    }

    int findLastAppear(const vector<int> &nums, int target){
        int left = 0, right = nums.size()-1;
        _____(left <= right){
            int mid = left + (right - left) / 2;
            __ (target __ nums[mid] && mid + 1 <= right && target __ nums[mid + 1]){
                left = mid + 1;
            }
            else __(target __ nums[mid]){
                r_ mid;
            }
            else __(target > nums[mid]){
                left = mid + 1;
            }
            else{
                right = mid - 1;
            }
        }
        r_ -1;
    }

    vector<int> searchRange(vector<int>& nums, int target) {
        r_ {findFirstAppear(nums, target), findLastAppear(nums, target)};
    }
};

/*
[]
0
[1,1,1,1]
1
[1,2,3,4,5]
3
[1,2,3,4,5]
6
*/
