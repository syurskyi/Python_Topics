___ test_jackpot(result):
    __ len(set(result)) == 1:
        return True
    else:
        return False

___ test():
    print("test has started")
    __ test_jackpot(['@', '@', '@', '@']) != True:
        print("error1")
    __ test_jackpot(['SS', 'SS', 'SS', 'Ss']) != False:
        print("error2")
