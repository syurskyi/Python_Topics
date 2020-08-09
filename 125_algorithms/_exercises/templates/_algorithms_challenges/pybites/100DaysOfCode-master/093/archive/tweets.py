______ csv
______ os
______ sys

DEFAULT_ARCHIVE = 'tweets.csv'


___ parse_csv(archive=DEFAULT_ARCHIVE
    __ not os.path.isfile(archive
        print('Please download archive and put in same folder as this script')
        sys.exit(1)

    with open(archive, 'r') as csvfile:
        ___ row in csv.DictReader(csvfile
            yield row
