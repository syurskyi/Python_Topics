/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-29 13:51:57
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
    bool isSymmetric(TreeNode* root) {
        r_ helper(root, root);
    }

    bool helper(TreeNode* lNode, TreeNode* rNode){
        __(lNode __ NULL || rNode __ NULL){
            r_ lNode __ rNode;
        }
        __(lNode->val != rNode->val){
            r_ false;
        }
        r_ helper(lNode->left, rNode->right) && helper(lNode->right, rNode->left);
    }
};

/*
[]
[1]
[1,2,3]
[1,2,2,3,4,4,3]
[1,2,2,null,3,null,3]
*/
