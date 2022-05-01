____ d.. _______ d..

_______ dateutil
____ d__.p.. _______ p..
____ d__.r.. _______ r..

??
c_ Actor:
    name: s..
    born: s..


??
c_ Movie:
    title: s..
    release_date: s..

actors [
    Actor('Wesley Snipes', 'July 31, 1962'),
    Actor('Robert de Niro', 'August 17, 1943'),
    Actor('Jennifer Aniston', 'February 11, 1969'),
    Actor('Mikey Rourke', 'September 16, 1952'),
    Actor('Al Pacino', 'July 31, 1962'),
    Actor('Alec Baldwin', 'July 31, 1962'),
    Actor('Michelle Pfeiffer', 'April 29, 1958'),
]
movies [
    Movie('New Jack City', 'January 17, 1991'),
    Movie('Goodfellas', 'October 19, 1990'),
    Movie('Horrible Bosses', 'September 16, 2011'),
    Movie('Harley Davidson and the Marlboro Man', 'December 28, 1991'),
    Movie('Heat', 'December 15, 1995'),
    Movie('Glengarry Glen Ross', 'September 29, 1992'),
    Movie('Scarface', 'March 12, 1984'),
]

___ get_age(actor: Actor, movie: Movie) __ s..
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} years old when {movie} came out.
       e.g.
       Wesley Snipes was 28 years old when New Jack City came out.
    """
    r.. _* actor.name} was {(relativedelta(p..(movie.release_date), p..(actor.born))).years} years old when {movie.title} came out.'

#print(get_age(actor, movie))