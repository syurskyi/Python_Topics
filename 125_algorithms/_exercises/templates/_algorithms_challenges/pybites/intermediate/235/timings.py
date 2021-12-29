import os
from pathlib import Path
from urllib.request import urlretrieve

tmp = Path(os.getenv("TMP", "/tmp"))
timings_log = tmp / 'pytest_timings.out'
__ not timings_log.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/pytest_timings.out',
        timings_log
    )


___ get_bite_with_fastest_avg_test(timings: list) -> str:
    """Return the bite which has the fastest average time per test"""
    # with open(timings) as f:
    #     data = [line.strip("\n") for line in f.readlines()]

    fastest_bite = []
    for test in timings:
        test_split = test.split(" ")

        __ len(test_split) != 8:
            continue
        
        bite_number = test_split[0]
        bite_tests = int(test_split[2])
        bite_time = float(test_split[5])
        fastest_bite.append([bite_number, (bite_time/bite_tests)])

    return sorted(fastest_bite, key=lambda x: x[1])[0][0]


# if __name__ == "__main__":
#     print(get_bite_with_fastest_avg_test(timings_log))