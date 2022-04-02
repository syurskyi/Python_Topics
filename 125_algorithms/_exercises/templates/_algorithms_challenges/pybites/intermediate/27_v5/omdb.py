_______ glob
_______ json
_______ os
_______ __
____ urllib.request _______ urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/omdb/'
MOVIES = ('bladerunner2049 fightclub glengary '
          'horrible-bosses terminator').s..
TMP = '/tmp'

# little bit of prework (yes working on pip installables ...)
___ movie __ MOVIES:
    fname = f'{movie}.json'
    remote = os.path.j..(BASE_URL, fname)
    local = os.path.j..(TMP, fname)
    urlretrieve(remote, local)

files = glob.glob(os.path.j..(TMP, '*json'))


___ get_movie_data(files=files
    result    # list
    ___ file __ files:
        w__ o.. file) __ f:
            result.a..(json.load(f))
    r.. result


___ get_single_comedy(movies
    r.. [m 'Title'  ___ m __ movies __ 'Comedy' __ m 'Genre' .s..(', ')][0]


___ get_movie_most_nominations(movies
    r = __.c..(r'(\d+) nomin')
    r.. s..([(m 'Title' , m 'Awards' ) ___ m __ movies], key=l.... x: i..(r.f..(x[1])[0]))[-1][0]


___ get_movie_longest_runtime(movies
    r = __.c..(r'(\d+) min')
    r.. s..([(m 'Title' , i..(r.f..(m 'Runtime' )[0])) ___ m __ movies], key=l.... x: -x[1])[0][0]
