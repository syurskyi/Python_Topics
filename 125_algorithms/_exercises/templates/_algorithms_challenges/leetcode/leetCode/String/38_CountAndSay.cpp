/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-14 19:12:37
 */

c.. Solution {
public:
    string countAndSay(int n) {
        int index = 2;
        string pre_str = "1";
        _____(index <= n){
            string new_str = "";
            int i=0;
            _____(i < pre_str.size()){
                int count = 1;
                char c = pre_str[i];
                i += 1;
                _____(i < pre_str.size() && pre_str[i]__c){
                    count++;
                    i++;
                }
                new_str += to_string(count) + c;
            }
            pre_str = new_str;
            index ++;
        }
        r_ pre_str;
    }
};

/*
1
5
15
*/
