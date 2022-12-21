/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-24 11:19:42
 */

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
c.. Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        __(root__NULL){
            r_ {};
        }
        vector<vector<int>> ans;
        deque<TreeNode*> levels{root};
        bool order=true;
        _____(!levels.empty()){
            vector<int> cur_level;
            int l_size = levels.size();
            ___(int i=0;i<l_size;i++){
                TreeNode* cur_node = levels.front();
                levels.pop_front();
                cur_level.push_back(cur_node->val);
                __(cur_node->left)  levels.push_back(cur_node->left);
                __(cur_node->right) levels.push_back(cur_node->right);
            }
            __(!order)  reverse(cur_level.begin(),cur_level.end());
            ans.push_back(cur_level);
            order = !order;
        }
        r_ ans;
    }
};

/*
[]
[1]
[1,2,3]
[0,1,2,3,4,5,6,null,null,7,null,8,9,null,10]
*/
