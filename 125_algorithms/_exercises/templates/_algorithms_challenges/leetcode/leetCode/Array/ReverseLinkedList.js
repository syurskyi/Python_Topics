/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */

// 翻转链表的思路
// 把head取出来，把head.next取出来，head.next.next也取出来。
// head.next = head
// 新的(head.next和head)与head.next.next进行新一轮交换。
// 直至空。
// PS，链表操作好麻烦。
 var reverseList = function(head) {

    let newHead = null

    // 先不判断进行一次交换
    let nHead = head
    __ (!nHead) {
        r_ null
    }
    let next = nHead.next
    __ (!next) {
        r_ nHead
    }
    let lNext = next.next

    next.next = nHead
    nHead.next = null

    newHead = next

    _____ (nHead && next && next.next) {
        nHead = lNext
        __ (!nHead) {
            r_ newHead
        }

        next = nHead.next

        __ (!next) {
            nHead.next = newHead
            r_ nHead
        }
        lNext = next.next

        next.next = nHead
        nHead.next = newHead

        newHead = next

    }
};