___ test_jackpot(result):
    __ l..(set(result)) __ 1:
        r.. True
    ____:
        r.. False

___ test():
    print("test has started")
    __ test_jackpot(['@', '@', '@', '@']) != True:
        print("error1")
    __ test_jackpot(['SS', 'SS', 'SS', 'Ss']) != False:
        print("error2")
