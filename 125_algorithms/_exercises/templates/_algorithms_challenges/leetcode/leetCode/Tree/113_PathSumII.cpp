/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-19 10:25:40
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
    vector<vector<int>> pathSum(TreeNode* root, int s..) {
        vector<vector<int>> pathList;
        vector<int> path;
        findPath(root, s.., path, pathList);
        r_ pathList;
    }

    void findPath(TreeNode* root, int s.., vector<int> path, vector<vector<int>> &pathList){
        __(root__NULL)  r_;
        path.push_back(root->val);
        __(root->left __ NULL && root->right__NULL && root->val__sum){
            pathList.push_back(path);
        }
        findPath(root->left, s..-root->val, path, pathList);
        findPath(root->right, s..-root->val, path, pathList);
        path.pop_back();
    }
};

/*
[]
0
[1,2,3,4,null,6,7,5,8]
15
[1,2,2,3,3,3,3]
6
*/
