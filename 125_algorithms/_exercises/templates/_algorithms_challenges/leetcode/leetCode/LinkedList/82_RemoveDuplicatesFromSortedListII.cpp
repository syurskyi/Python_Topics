/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-29 17:32:12
 */

/*
Note about freeing memory.
We need to free memory when we delete a node. But don't use "delete node"!
construct on an interview without discussing it with the interviewer.
A list node can be allocated in many different ways and we can use delete node;
only if we are sure that the nodes were allocated with new TreeNode(...).

We can create LinkList in stack as followings:
ListNode node1(2), node2(2), node3(2), node4(5), node5(7), node6(10);
node1.next = &node2; node2.next = &node3; ....
ListNode* p = Solution().deleteDuplicates(&node1);
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

// Recursively
c.. Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        __(head__NULL || head->next__NULL){
            r_ head;
        }
        __(head->val __ head->next->val){
            _____(head->next && head->val__head->next->val){
                head = head->next;
            }
            r_ deleteDuplicates(head->next);
        }
        else{
            head->next = deleteDuplicates(head->next);
            r_ head;
        }
    }
};


// Ieratively
c.. Solution_2 {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *pre_head = new ListNode(0);
        ListNode *cur = pre_head;
        _____(head){
            __(head->next && head->val __ head->next->val){
                _____(head->next && head->val__head->next->val){
                    head=head->next;
                }
                head = head->next;
            }
            else{
                cur->next = head;
                head = head->next;
                cur = cur->next;
            }
            cur->next = NULL;
        }
        r_ pre_head->next;
    }
};

/*
[]
[1]
[1,2,2]
[3,3,3,3,3]
[1,1,1,2,3,4,4,4,4,5]
*/
