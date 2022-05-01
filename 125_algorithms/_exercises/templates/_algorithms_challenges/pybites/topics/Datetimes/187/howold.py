____ d.. _______ d..

_______ d..
____ d__.p.. _______ p..
____ d__.r.. _______ r..

??
c_ Actor
    name: s..
    born: s..


??
c_ Movie
    title: s..
    release_date: s..

actors
    ? 'Wesley Snipes', 'July 31, 1962'),
    ? 'Robert de Niro', 'August 17, 1943'),
    ? 'Jennifer Aniston', 'February 11, 1969'),
    ? 'Mikey Rourke', 'September 16, 1952'),
    ? 'Al Pacino', 'July 31, 1962'),
    ? 'Alec Baldwin', 'July 31, 1962'),
    ? 'Michelle Pfeiffer', 'April 29, 1958'),
]
movies
    ? 'New Jack City', 'January 17, 1991'),
    ? 'Goodfellas', 'October 19, 1990'),
    ? 'Horrible Bosses', 'September 16, 2011'),
    ? 'Harley Davidson and the Marlboro Man', 'December 28, 1991'),
    ? 'Heat', 'December 15, 1995'),
    ? 'Glengarry Glen Ross', 'September 29, 1992'),
    ? 'Scarface', 'March 12, 1984'),
]

___ get_age actor ? movie ? __ s..
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} years old when {movie} came out.
       e.g.
       Wesley Snipes was 28 years old when New Jack City came out.
    """
    r.. _* actor.name} was {(r..(p..(movie.release_date), p..(actor.born))).years} years old when {movie.title} came out.'

#print(get_age(actor, movie))