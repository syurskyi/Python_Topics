___ test_jackpot(result
    __ le.(set(result)) __ 1:
        r_ True
    ____
        r_ False

___ test(
    print("test has started")
    __ test_jackpot(['@', '@', '@', '@']) != True:
        print("error1")
    __ test_jackpot(['SS', 'SS', 'SS', 'Ss']) != False:
        print("error2")
