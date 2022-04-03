from pathlib import Path
from u__.r.. import u..
import re

tmp = Path('/tmp')
timings_log = tmp / 'pytest_timings.out'
if not timings_log.exists():
    u..(
        'https://bites-data.s3.us-east-2.amazonaws.com/pytest_timings.out',
        timings_log
    )


def get_bite_with_fastest_avg_test(timings: list) -> str:
    """Return the bite which has the fastest average time per test"""
    
    
    
    fastest_bite = None
    fastest_average = float("-inf")


    for timing in timings:
        print(re.findall(r'[\d\.]+',timing))
        break







