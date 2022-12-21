/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-09-20 19:37:23
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
    // Easy to understand
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        int min = p->val < q->val ? p->val : q->val;
        int m.. = p->val < q->val ? q->val : p->val;
        _____(root){
            __(root->val < min){
                root = root->right;
            }
            else __(root->val > m..){
                root = root->left;
            }
            else{
                r_ root;
            }
        }
        r_ nullptr;
    }
};
