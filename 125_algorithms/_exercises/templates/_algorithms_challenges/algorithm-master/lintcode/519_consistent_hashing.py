c_ Solution:
    """
    @param: n: a positive integer
    @return: n x 3 matrix
    """
    ___ consistentHashing  n
        res [[0, 359, 1]]
        __ n.. isi..(n, i..) \
            o. n < 2:
            r.. res
        ti 0 # ti: target_index for the **upcoming** machine in results
        # mi: machine_index for the **upcoming** machines in results
        # for n is 5: got [1, 2, 3, 4]
        ___ mi __ r..(1, n
            ti 0
            # emi: existing_machine_index for the **existing** machines in results
            # for n is 5 and will add last machine: got [0, 1, 2, 3]
            ___ emi __ r..(mi
                # Before adding each machine, check the current maximum partition
                __ res[emi][1] - res[emi][0] > res[ti][1] - res[ti][0]:
                    ti emi
            x, y res[ti][0], res[ti][1]
            res[ti][1] (x + y) / 2
            res.a..([(x + y) / 2 + 1, y, mi + 1])
        r.. s..(res, k.._l.... item: item 0
