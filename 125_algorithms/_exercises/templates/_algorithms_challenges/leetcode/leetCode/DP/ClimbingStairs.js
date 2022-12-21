/**
 * @param {number} n
 * @return {number}
 */
 var climbStairs = function(n) {
    let dp = [
        1,
        2
    ]
    
    __ (n <= 2) {
        r_ dp[n-1]
    }

    ___ (let i=2;i<n;i++) {
        dp.push(dp[i-2]+dp[i-1])
    }
    r_ dp[n-1]
};