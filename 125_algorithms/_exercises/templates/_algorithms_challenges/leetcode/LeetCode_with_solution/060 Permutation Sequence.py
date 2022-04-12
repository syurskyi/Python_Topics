"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""
_______ m__

__author__ 'Danyang'


c_ Solution(o..
    ___ getPermutation  n, k
        k -_ 1

        array r..(1, n+1)
        k %= m__.factorial(n)
        ret    # list
        ___ i __ x..(n-1, -1, -1
            idx, k divmod(k, m__.factorial(i
            ret.a..(array.p.. idx

        r.. "".j.. m..(s.., ret

    ___ getPermutation  n, k
        """
        Reverse Cantor Expansion

        equation: sum a_i * i! = k
        :param n: integer
        :param k: integer
        :return: String
        """
        # factorial
        fac [1 ___ _ __ x..(n)]
        ___ i __ x..(1, n
            fac[i] fac[i-1]*i

        # solve equation
        k -_ 1  # index starting from 0
        a [0 ___ _ __ x..(n)]
        ___ i __ x..(n-1, -1, -1
            a[n-1-i] k/fac[i]  # a[i] = k/fac[i]
            k %= fac[i]

        # post-process
        candidate r..(1, n+1)  # sorted
        visited [F.. ___ _ __ x..(n)]
        ___ ind, val __ e..(a
            i 0  # pointer
            cnt 0  # counter
            w... T...
                __ visited[i]:
                    i += 1
                ____
                    __ cnt __ val: _____
                    cnt += 1
                    i += 1

            a[ind] candidate[i]
            visited[i] T..

        r.. "".j.. m..(s.., a

    ___ getPermutation_complicated  n, k
        """
        Mathematics
        Reversed Cantor Expansion

        A = [1, 2, ..., n], where A's index starts from 0
        Suppose for n element, the k-th permutation is:
        [a0, a1, a2, ..., an-1]

        since [a1, a3, ..., an-1] has (n-1)! permutations,
        if k < (n-1)!, a0 = A[0] (first element in array), else a0 = A[k/(n-1)!] (subsequent items)

        recursively, (or iteratively)
        a0 = A[k0/(n-1)!], where k0 = k
        a1 = A[k1/(n-2)!], where k1 = k0%(n-1)! in the remaining array
        a2 = A[k2/(n-3)!], where k2 = k1%(n-2)! in the remaining array
        ...

        :param n: integer
        :param k: integer
        :return: String
        """
        k -_ 1  # index starting from 0

        factorial 1  # (n-1)!
        ___ i __ x..(1, n
            factorial *= i

        result    # list
        array r..(1, n+1)
        ___ i __ r..(x..(1, n:
            index k/factorial
            result.a..(array[index])
            array array[:index]+array[index+1:]
            k k%factorial
            factorial /= i

        # case when factorial=0!
        result.a..(array 0

        r.. "".j..(s..(element) ___ element __ result)


c_ Solution_TLE:
    """
    Time Limit Expected
    """

    ___ -
        counter 0

    ___ getPermutation  n, k
        """
        dfs, iterate all possibilities
        :param n: integer
        :param k: integer
        :return: String
        """
        __ n.. n:
            r..

        sequence r..(1, n+1)
        result get_kth_permutation_dfs(sequence, k, [])
        r.. "".j..(s..(element) ___ element __ result)


    ___ get_kth_permutation_dfs  remaining_seq, k, cur
        """
        dfs until find kth permutation, return that permutation, otherwise return None
        :param remaining_seq:
        :param k:
        :param cur:
        :return:
        """
        __ n.. remaining_seq:
            counter += 1
            __ counter __ k:
                r.. cur

        ___ ind, val __ e..(remaining_seq
            result get_kth_permutation_dfs(remaining_seq[:ind]+remaining_seq[ind+1:], k, cur+[val])
            __ result: r.. result


__ _______ __ _______
    ... Solution().getPermutation(4, 6) __ "1432"
    ... Solution().getPermutation(2, 2) __ "21"
    ... Solution().getPermutation(3, 1) __ "123"
    ... Solution().getPermutation(3, 5) __ "312"
    print Solution().getPermutation(9, 171669)