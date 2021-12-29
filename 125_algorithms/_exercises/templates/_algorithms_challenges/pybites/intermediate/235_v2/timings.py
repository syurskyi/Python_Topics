from pathlib import Path
from urllib.request import urlretrieve
import re

tmp = Path('/tmp')
timings_log = tmp / 'pytest_timings.out'
__ not timings_log.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/pytest_timings.out',
        timings_log
    )


___ get_bite_with_fastest_avg_test(timings: list) -> str:
    """Return the bite which has the fastest average time per test"""
    
    
    
    fastest_bite = None
    fastest_average = float("-inf")


    for timing in timings:
        print(re.findall(r'[\d\.]+',timing))
        break







