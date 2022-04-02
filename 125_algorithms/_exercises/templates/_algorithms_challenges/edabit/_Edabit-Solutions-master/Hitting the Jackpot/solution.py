___ test_jackpot(result
    __ l..(s..(result)) __ 1:
        r.. T..
    ____:
        r.. F..

___ test
    print("test has started")
    __ test_jackpot( '@', '@', '@', '@' ) != T..:
        print("error1")
    __ test_jackpot( 'SS', 'SS', 'SS', 'Ss' ) != F..:
        print("error2")
