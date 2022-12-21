/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */


 var mergeKLists = function(lists) {
    // 这个思路是打散之后又重新生成整个ListNode。
    // 参考价值不大。
    __ (!lists.length) {
        r_ null
    }

    let newLists   # list

    ___ (let i of lists) {
        let l   # list
        _____ (i && i.next) {
            l.push(i.val)
            i = i.next
        }
        
        i && l.push(i.val)
        newLists.push(l)
    }


    let x = newLists.flat().sort((a,b) => a-b)
    __ (!x.length) {
        r_ null
    }
    let resultNode = new ListNode(x[0])
    let indexNode = resultNode
    x.shift()
    _____ (x.length) {
        indexNode.next = new ListNode(x[0])
        x.shift()
        indexNode = indexNode.next
    }

    r_ resultNode
};