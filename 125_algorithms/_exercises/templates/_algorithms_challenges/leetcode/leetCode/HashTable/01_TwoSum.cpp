/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-14 10:43:27
 */


c.. Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> hash;
        ___(int i=0;i<nums.size();i++){
            int other_n = target - nums[i];
            __(hash.find(other_n) != hash.end()){
                r_ {i, hash[other_n]};
            }
            hash[nums[i]] = i;
        }
    }
};
/*
[1,2]
3
[3,2,4]
6
*/
