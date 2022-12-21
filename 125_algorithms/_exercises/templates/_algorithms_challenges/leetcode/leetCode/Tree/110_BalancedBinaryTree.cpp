/*
* @Author: xuelangZF
* @Date:   2016-03-06 17:16:31
* @Last Modified by:   xuelangZF
* @Last Modified time: 2016-03-06 17:16:31
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
    bool isBalancedSolution(TreeNode* root, int &height){
        __(!root){
            r_ true;
        }
        int left = 0;
        int right = 0;
        __ (isBalancedSolution(root->left, left) && isBalancedSolution(root->right, right)){
            int diff = left - right;
            __ (diff < -1 or diff > 1){
                r_ false;
            }
            height = (left > right ? left: right) + 1;
            r_ true;
        }
        r_ false;
    }
    bool isBalanced(TreeNode* pRoot) {
        int height = 0;
        r_ isBalancedSolution(pRoot, height);
    }
};
