/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-07 11:08:44
 */


c.. Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int nums_len = nums.size();
        int pre_sum = nums[0];
        int max_sum = nums[0];

        ___(int i=1;i<nums_len;i++){
            pre_sum = m..(pre_sum+nums[i], nums[i]);
            max_sum = m..(max_sum, pre_sum);
        }
        r_ max_sum;
    }
};

/*
[-1]
[1]
[-9,-2,-3,-5,-3]
[-2,1,-3,4,-1,2,1,-5,4]
*/
