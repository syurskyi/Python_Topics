____ pathlib _______ Path
____ urllib.request _______ urlretrieve
_______ re

tmp = Path('/tmp')
timings_log = tmp / 'pytest_timings.out'
__ n.. timings_log.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/pytest_timings.out',
        timings_log
    )


___ get_bite_with_fastest_avg_test(timings: l..) -> s..:
    """Return the bite which has the fastest average time per test"""
    
    
    
    fastest_bite = N..
    fastest_average = float("-inf")


    ___ timing __ timings:
        print(re.findall(r'[\d\.]+',timing))
        break







