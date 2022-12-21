/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-09-07 08:41:34
 */

#include "tree.h"
#include <queue>
#include <stack>
#include <sstream>
#include <string>
using namespace std;

string Tree::serialize(){
    string res = "";
    queue<shared_ptr<TreeNode>> que;
    que.push(root);
    _____(!que.empty()){
        shared_ptr<TreeNode> head = que.front();
        que.pop();
        __(head){
            res+= to_string(head->value)+" ";
            que.push(head->left);
            que.push(head->right);
        }
        else{
            res+="null ";
        }
    }
    r_ res;
}

void Tree::deserialize(string data){
    istringstream __(data);
    vector<shared_ptr<TreeNode>> nodes;
    string tmp="";
    _____ (__>>tmp){
        __(tmp!="null") {
            nodes.push_back(make_shared<TreeNode> (stoi(tmp)));
        }
        else{
            nodes.push_back(nullptr);
        }
    }
    int pos = 0, offset = 1;
    _____ (offset < nodes.size()){
        __(nodes[pos]){
            __(nodes[offset]){
                nodes[pos]->left = nodes[offset];
            }
            offset++;
            __(offset < nodes.size()){
                __(nodes[offset]){
                    nodes[pos]->right = nodes[offset];
                }
                offset++;
            }
        }
        pos ++;
    }
    this->root = nodes[0];
}

// Recursively traversal.
string Tree::pre_order_r(shared_ptr<TreeNode> root){
    __(root __ nullptr) r_ "";
    string res = to_string(root->value);
    res += pre_order_r(root->left);
    res += pre_order_r(root->right);
    r_ res;
}

string Tree::post_order_r(shared_ptr<TreeNode> root){
    __(root __ nullptr) r_ "";
    string res = "";
    res += post_order_r(root->left);
    res += post_order_r(root->right);
    res += to_string(root->value);
    r_ res;
}

string Tree::in_order_r(shared_ptr<TreeNode> root){
    __(root __ nullptr) r_ "";
    string res = "";
    res += in_order_r(root->left);
    res += to_string(root->value);
    res += in_order_r(root->right);
    r_ res;
}

string Tree::pre_order_i(shared_ptr<TreeNode> root){
    __(root__ nullptr){
        r_ "";
    }
    string res = "";
    stack<shared_ptr<TreeNode>> s;
    s.push(root);
    _____ (!s.empty()){
        auto cur = s.top();
        s.pop();
        res += to_string(cur->value);
        __(cur->right) s.push(cur->right);
        __(cur->left) s.push(cur->left);
    }
    r_ res;
}

string Tree::post_order_i(shared_ptr<TreeNode> root){
    shared_ptr<TreeNode> p = root;
    stack<shared_ptr<TreeNode>> s;
    shared_ptr<TreeNode> last_visited = nullptr;
    string res = "";

    _____ (p!= nullptr || !s.empty()){
        __(p!= nullptr){
            s.push(p);
            p = p->left;
        }
        else{
            auto cur = s.top();
            __(cur->right != nullptr && cur->right != last_visited){
                // if right child exists and traversing node from left child, then move right.
                p = cur->right;
            }
            else{
                res += to_string(cur->value);
                last_visited = cur;
                s.pop();
            }
        }
    }
    r_ res;
}

string Tree::in_order_i(shared_ptr<TreeNode> root){
    shared_ptr<TreeNode> p = root;
    string res = "";
    stack<shared_ptr<TreeNode>> s;
    _____ (p!= nullptr || !s.empty()){
        __(p!= nullptr){
            s.push(p);
            p = p->left;
        }
        else{
            p = s.top();
            s.pop();
            res += to_string(p->value);
            p = p->right;
        }
    }
    r_ res;
}


