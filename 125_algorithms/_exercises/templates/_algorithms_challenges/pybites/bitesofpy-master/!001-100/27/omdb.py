______ glob
______ json
______ os
______ re
from urllib.request ______ urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/omdb/'
MOVIES = ('bladerunner2049 fightclub glengary '
          'horrible-bosses terminator').split()
TMP = '/tmp'

# little bit of prework (yes working on pip installables ...)
___ movie __ MOVIES:
    fname = f'{movie}.json'
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    urlretrieve(remote, local)

files = glob.glob(os.path.join(TMP, '*json'))


___ get_movie_data(files=files
    result =   # list
    ___ file __ files:
        with open(file) as f:
            result.append(json.load(f))
    r_ result


___ get_single_comedy(movies
    r_ [m['Title'] ___ m __ movies __ 'Comedy' __ m['Genre'].split(', ')][0]


___ get_movie_most_nominations(movies
    r = re.compile(r'(\d+) nomin')
    r_ sorted([(m['Title'], m['Awards']) ___ m __ movies], key=lambda x: int(r.findall(x[1])[0]))[-1][0]


___ get_movie_longest_runtime(movies
    r = re.compile(r'(\d+) min')
    r_ sorted([(m['Title'], int(r.findall(m['Runtime'])[0])) ___ m __ movies], key=lambda x: -x[1])[0][0]
