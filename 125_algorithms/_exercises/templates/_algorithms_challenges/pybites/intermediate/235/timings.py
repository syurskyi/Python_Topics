_______ __
____ p.. _______ P..
____ u__.r.. _______ u..

tmp  P.. __.g.. "TMP", "/tmp"
timings_log tmp / 'pytest_timings.out'
__ n.. timings_log.exists
    u..(
        'https://bites-data.s3.us-east-2.amazonaws.com/pytest_timings.out',
        timings_log
    )


___ get_bite_with_fastest_avg_test(timings: l..) __ s..
    """Return the bite which has the fastest average time per test"""
    # with open(timings) as f:
    #     data = [line.strip("\n") for line in f.r..]

    fastest_bite    # list
    ___ test __ timings:
        test_split test.s..(" ")

        __ l..(test_split) !_ 8:
            _____
        
        bite_number test_split[0]
        bite_tests i..(test_split[2])
        bite_time f__(test_split[5])
        fastest_bite.a..([bite_number, (bite_time/bite_tests)])

    r.. s..(fastest_bite, k.._l.... x: x[1]) 0 0 


# if __name__ == "__main__":
#     print(get_bite_with_fastest_avg_test(timings_log))