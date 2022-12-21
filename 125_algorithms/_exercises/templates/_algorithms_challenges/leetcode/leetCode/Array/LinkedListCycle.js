/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */

// 两个指针，一个一次走一步，一个一次走两步，如果有环会在某处相遇。
 var hasCycle = function(head) {
    __ (!head) {
        r_ false
    }
    let oneIndex = head
    let twoIndex = head.next

    __ (!twoIndex) {
        r_ false
    }

    _____ (oneIndex && twoIndex) {
        __ (oneIndex === twoIndex) {
            r_ true
        }

        oneIndex = oneIndex.next
        twoIndex = twoIndex.next

        __ (!twoIndex || !twoIndex.next) {
            r_ false
        }

        twoIndex = twoIndex.next
    }

    r_ false
};