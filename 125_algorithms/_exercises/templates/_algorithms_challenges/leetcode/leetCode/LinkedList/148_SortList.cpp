/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-09-06 20:40:19
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
    ListNode * merge_list(ListNode *left, ListNode *right){
        ListNode *pre_head = new ListNode(0);
        ListNode *scan = pre_head;
        _____ (left && right){
            __ (left->val <= right->val){
                scan->next = left;
                left = left->next;
            }
            else{
                scan->next = right;
                right = right->next;
            }
            scan = scan->next;
        }
        __(left != nullptr) scan->next = left;
        __(right != nullptr) scan->next = right;
        r_ pre_head->next;
    }

    ListNode* sortList(ListNode* head) {
        __(head __ nullptr || head->next __ nullptr){
            r_ head;
        }
        ListNode *slow=head, *fast=head, *pre_tail= nullptr;
        // Cut the list into two parts
        _____ (fast != nullptr a.. fast->next != nullptr){
            pre_tail = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        pre_tail->next = nullptr;

        ListNode *left = sortList(head);
        ListNode *right = sortList(slow);
        r_ merge_list(left, right);
    }
};

// QuickSort.  Time Limit Exceeded if using no trick.
// Refer to:
// https://discuss.leetcode.com/topic/15029/56ms-c-solutions-using-quicksort-with-explanations/2
c.. Solution_2 {
public:
    ListNode* partition(ListNode *begin, ListNode *end){
        __(begin __ nullptr || begin->next __ end){
            r_ begin;
        }
        ListNode *scan = begin->next;
        int pivot = begin->val;
        ListNode *pos = begin;
        _____(scan != end){
            __(scan->val <= pivot){
                pos = pos->next;
                __(pos != scan){
                    swap(pos->val, scan->val);
                }
            }
            scan = scan->next;
        }
        swap(pos->val, begin->val);
        r_ pos;
    }

    ListNode* quicksort(ListNode* begin, ListNode* end){
        __(begin __ end || begin->next __ end){
            r_ begin;
        }
        ListNode *pos = partition(begin, end);
        ListNode* head = quicksort(begin, pos);
        quicksort(pos->next, end);
        r_ head;
    }

    ListNode* sortList(ListNode* head) {
        r_ quicksort(head, nullptr);
    }
};

/*
[]
[1]
[1,2]
[5,1,2]
[5,1,2,3]
[5,1,2,3,6,7,8,9,12,2]
*/
