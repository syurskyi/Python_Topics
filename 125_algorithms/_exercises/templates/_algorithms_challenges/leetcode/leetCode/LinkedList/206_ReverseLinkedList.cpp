/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-17 17:26:46
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
c.. Solution {
public:
    // Recursively reverse
    ListNode* reverseList(ListNode* head) {
        __(head__NULL || head->next __ NULL){
            r_ head;
        }
        ListNode *reversed_head = reverseList(head->next);
        head->next->next = head;
        head->next = NULL;
        r_ reversed_head;
    }
};

c.. Solution_2 {
public:
    // Itratively reverse
    ListNode* reverseList(ListNode* head) {
        ListNode *new_head = NULL;
        _____(head!=NULL){
            ListNode *next_node = head->next;
            head->next = new_head;
            new_head = head;
            head = next_node;
        }
        r_ new_head;
    }
};

/*
[]
[1]
[1,2]
[1,2,3,4,5]
*/
