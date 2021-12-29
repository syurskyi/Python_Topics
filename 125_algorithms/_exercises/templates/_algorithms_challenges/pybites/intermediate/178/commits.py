____ collections _______ Counter
_______ os
_______ re
____ urllib.request _______ urlretrieve

____ dateutil.parser _______ parse

commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


___ get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = N..) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """


    month_changes = Counter()


    with open(commit_log,'r') as f:
        ___ line __ f:
            date_section, change_section = line.split('|')
            date = parse(date_section,fuzzy=True)
            
            __ year:
                __ date.year < year:
                    break
                __ date.year > year:
                    continue

            numbers = re.findall(r'(\d+) (?:insertions|deletions)',change_section)

            changes= s..(map(int,numbers))


            month_changes[date.strftime('%Y-%m')] += changes




    values = month_changes.most_common()


    r.. values[-1][0],values[0][0]

__ __name__ __ "__main__":
    get_min_max_amount_of_commits()



