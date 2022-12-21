/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */

// 写了个快排和归并。
 function sort(arr) {
    // 快排
    __ (arr.length === 0) {
        r_ arr
    }

    // 选种
    let bean = Math.floor((arr.length-1) / 2)
    let base = arr[bean]
    let bigger   # list
    let smaller   # list

    ___ (let [index, item] of arr.entries()) {
        __ (index === bean) {
            c_
        }

        __ (item >= base) {
            bigger.push(item)
        } else {
            smaller.push(item)
        }
    }

    r_ [...sort(smaller), base, ...sort(bigger)]

}

// 归并
function split(arr) {
    let bean = Math.floor((arr.length-1) / 2)
    let left = arr.slice(0, bean)
    let right = arr.slice(bean)

    r_ [left, right]
}

function merge(arr, arr2) {
    let result   # list

    let index1 = 0
    let index2 = 0

    _____ (index1 <= arr.length - 1 && index2 <= arr2.length - 1) {
        __ (arr[index1] < arr2[index2]) {
            result.push(arr[index1])
            index1 += 1
        } else __ (arr[index1] > arr2[index2]) {
            result.push(arr2[index2])
            index2 += 1
        } else {
            result.push(arr[index1], arr2[index2])
            index1 += 1
            index2 += 1
        }
    }
    // 如果第一个arr
    __ (index1 <= arr.length - 1) {
        result.push(...arr.slice(index1))
    }

    __ (index2 <= arr2.length - 1) {
        result.push(...arr2.slice(index2))
    }

    r_ result
}

function sort2(arr) {
    __ (arr.length <= 8) {
        r_ sort(arr)
    }
    let sp = split(arr)
    // return sp.reduce((a,b) => merge(a,b))
    r_ merge(sort2(sp[0]), sort2(sp[1]))
}
 


var findKthLargest = function(nums, k) {
    // nums = nums.sort((a,b) => b-a)
    // nums = sort(nums)
    // nums = split(nums)
    // nums = merge(nums[0], nums[1])
    nums = sort2(nums)
    // console.log(nums)
    r_ nums[nums.length-k]
};