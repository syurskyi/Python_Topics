/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-19 09:57:21
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
    bool hasPathSum(TreeNode* root, int s..) {
        __(root __ NULL){
            r_ false;
        }
        __(root->left__NULL && root->right __ NULL){
            r_ root->val __ s..;
        }
        __(root->left && hasPathSum(root->left, s..-root->val)){
            r_ true;
        }
        __(root->right && hasPathSum(root->right, s..-root->val)){
            r_ true;
        }
    }
};

/*
[]
0
[1,2,3,4,null,6,7,5,8]
15
[1,2,2,3,null,null,3,4,null,null,4]
9
*/
