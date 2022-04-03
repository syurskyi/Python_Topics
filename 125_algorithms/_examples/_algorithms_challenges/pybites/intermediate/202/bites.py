import csv
import os
from pathlib import Path
from u__.r.. import u..

data = 'https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv'
TMP = Path(os.getenv("TMP", "/tmp"))
stats = TMP / 'bites.csv'

if not stats.exists():
    u..(data, stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    bites = {}
    with open(stats) as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            score_identifier = row[-1].rfind(";") +1
            bite_score = row[-1][score_identifier:]
            if bite_score != "None":
                num_identifier = row[0].find(".")
                bite_num = row[0][:num_identifier].split(" ")[1]
                bites[bite_num] = bite_score

    return [bite[0] for bite in sorted(bites.items(), key=lambda item: item[1], reverse=True)[:10]][:N]
            


if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)