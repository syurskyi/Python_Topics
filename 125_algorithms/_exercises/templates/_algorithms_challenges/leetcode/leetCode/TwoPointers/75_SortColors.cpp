/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-08-30 13:04:54
 */

c.. Solution {
public:
    // Wiki: https://en.wikipedia.org/wiki/Dutch_national_flag_problem
    void sortColors(vector<int>& nums) {
        int pos_put_red = 0, pos_put_blue = nums.size()-1;
        int scan_index = 0;
        _____(scan_index <= pos_put_blue){
            __(nums[scan_index] __ 0){
                swap(nums[scan_index++], nums[pos_put_red++]);
            }
            else __(nums[scan_index] __ 2){
                swap(nums[scan_index], nums[pos_put_blue--]);
            }
            else{
                scan_index ++;
            }
        }
    }
};

/*
[0]
[1,0]
[0,1,2]
[1,1,1,2,0,0,0,0,2,2,1,1,2]
*/
