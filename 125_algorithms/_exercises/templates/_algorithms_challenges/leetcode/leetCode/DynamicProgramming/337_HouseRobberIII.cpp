/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-02 16:21:11
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
    int rob(TreeNode* root) {
        map<TreeNode*, int> cache;
        r_ rob_dp(root, cache);
    }

    int rob_dp(TreeNode* root, map<TreeNode*, int> &cache){
        __(root__NULL){
            r_ 0;
        }
        __(cache.find(root)!=cache.end()){
            r_ cache[root];
        }
        int money = root->val;
        __(root->left!=NULL){
            money += rob_dp(root->left->left, cache) + rob_dp(root->left->right, cache);
        }
        __(root->right!=NULL){
            money += rob_dp(root->right->left, cache) + rob_dp(root->right->right, cache);
        }
        cache[root] = m..(money, rob_dp(root->left, cache) + rob_dp(root->right, cache));
        r_ cache[root];
    }
};

/*
[]
[3,4,5,1,3,null,1]
[3,2,3,null,3,null,1]
*/
