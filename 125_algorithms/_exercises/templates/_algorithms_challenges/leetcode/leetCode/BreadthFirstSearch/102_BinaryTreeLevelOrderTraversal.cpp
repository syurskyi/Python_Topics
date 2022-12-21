/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-24 10:59:23
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        __(root__NULL){
            r_ {};
        }
        vector<vector<int>> ans;
        deque<TreeNode*> levels{root};
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
            ans.push_back(cur_level);
        }
        r_ ans;
    }
};


/*
[]
[1]
[1,2,3]
[3,9,20,null,null,15,7]
*/
