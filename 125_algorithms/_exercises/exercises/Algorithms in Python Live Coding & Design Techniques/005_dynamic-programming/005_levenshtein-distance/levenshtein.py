
# Recursive Approach
___ get_edit_dist(str1, str2, m, n
    __ m __ 0 or n __ 0:
        r_ ma_(m, n)

    ch1 = 1 + get_edit_dist(str1, str2, m, n - 1)
    ch2 = 1 + get_edit_dist(str1, str2, m - 1, n)

    __ str1[m-1] __ str2[n-1]:
        k = 0
    ____
        k = 1

    ch3 = k + get_edit_dist(str1, str2, m - 1, n - 1)
    r_ min(ch1, ch2, ch3)


# DP : Top Down Approach
___ get_edit_dist_td(str1, str2, m, n, dp
    __ m __ 0 or n __ 0:
        r_ ma_(m, n)

    __ dp[m-1][n-1] >= 0:
        r_ dp[m-1][n-1]

    ch1 = 1 + get_edit_dist_td(str1, str2, m, n - 1, dp)
    ch2 = 1 + get_edit_dist_td(str1, str2, m - 1, n, dp)

    __ str1[m - 1] __ str2[n - 1]:
        k = 0
    ____
        k = 1

    ch3 = k + get_edit_dist_td(str1, str2, m - 1, n - 1, dp)
    dp[m-1][n-1] = min(ch1, ch2, ch3)
    r_ dp[m-1][n-1]


# DP : Bottom Up Approach
___ get_edit_dist_bu(str1, str2, m, n
    l_dist = [[0 ___ i __ ra__(n+1)]___ i __ ra__(m+1)]

    ___ i __ ra__(m
        l_dist[0][i] = i
    ___ j __ ra__(n
        l_dist[j][0] = j
    ___ i __ ra__(1, m+1
        ___ j __ ra__(1, n+1
            __ str1[i - 1] __ str2[j - 1]:
                l_dist[i][j] = l_dist[i - 1][j - 1]
            ____
                l_dist[i][j] = min(l_dist[i][j - 1], l_dist[i - 1][j], l_dist[i - 1][j - 1]) + 1;
    r_ l_dist[m][n]



___ editDistDP(str1, str2, m, n 
    # Create a table to store results of subproblems 
    dp = [[0 ___ x __ ra__(n + 1)] ___ x __ ra__(m + 1)]
  
    # Fill d[][] in bottom up manner 
    ___ i __ ra__(m + 1
        ___ j __ ra__(n + 1
  
            # If first string is empty, only option is to 
            # insert all characters of second string 
            __ i __ 0: 
                dp[i][j] = j    # Min. operations = j 
  
            # If second string is empty, only option is to 
            # remove all characters of second string 
            ____ j __ 0: 
                dp[i][j] = i    # Min. operations = i 
  
            # If last characters are same, ignore last char 
            # and recur for remaining string 
            ____ str1[i-1] __ str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
  
            # If last character are different, consider all 
            # possibilities and find minimum 
            ____
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])    # Replace 
  
    r_ dp[m][n] 


__ ___ __ '__main__':
    str1 = 'Base'
    str2 = 'Basic'
    m = le_(str1)
    n = le_(str2)
    print(get_edit_dist(str1, str2, m, n))

    dp = [[-1 ___ i __ ra__(n)]___ i __ ra__(m)]
    print('top down: ', get_edit_dist_td(str1, str2, m, n, dp))

    print('bottom up: ', get_edit_dist_bu(str1, str2, m, n))
