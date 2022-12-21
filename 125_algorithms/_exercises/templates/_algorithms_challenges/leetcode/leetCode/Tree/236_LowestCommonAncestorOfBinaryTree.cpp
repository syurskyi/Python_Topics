/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-09-16 12:35:32
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
    /*
    Recursive method: DFS.
    If the current (sub)tree contains both p and q, then the function result is their LCA.
    If only one of them is in that subtree, then the result is that one of them.
    If neither are in that subtree, the result is null/None/nil.

    More version can be found here:
    https://discuss.leetcode.com/topic/18561/4-lines-c-java-python-ruby
    */
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        __(root__NULL || root__p || root__q){
            r_ root;
        }
        TreeNode* l = lowestCommonAncestor(root->left, p, q);
        TreeNode* r = lowestCommonAncestor(root->right, p, q);
        __(l && r){
            r_ root;
        }
        else{
            r_ l ? l : r;
        }
    }
};

c.. Solution_2 {
public:
    /*
    Iteratice method.
    */
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        map<TreeNode*, TreeNode*> parent;
        parent.insert({root, NULL});
        queue<TreeNode*> que;
        que.push(root);
        // Build the relationship from child to parent
        _____(parent.find(p) __ parent.end() || parent.find(q) __ parent.end()){
            TreeNode *cur = que.front();
            que.pop();
            __(cur->left){
                que.push(cur->left);
                parent.insert({cur->left, cur});
            }
            __(cur->right){
                que.push(cur->right);
                parent.insert({cur->right, cur});
            }
        }
        // Trace brack from one node, record the path. Then trace from the other.
        s..<TreeNode*> ancestor;
        _____(p){
            ancestor.insert(p);
            p = parent[p];
        }
        _____(ancestor.find(q) __ ancestor.end()){
            q = parent[q];
        }
        r_ q;
    }
};

