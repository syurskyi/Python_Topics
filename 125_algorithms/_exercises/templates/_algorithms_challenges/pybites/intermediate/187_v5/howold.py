____ d.. _______ d..
____ dateutil.parser _______ p..
____ d__.r.. _______ r..

RETURN_FORMAT '{name} was {age} years old when {movie} came out.'


??
c_ Actor:
    name: s..
    born: s..


??
c_ Movie:
    title: s..
    release_date: s..


___ get_age(actor: Actor, movie: Movie) __ s..
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} years old when {movie} came out.
       e.g.
       Wesley Snipes was 28 years old when New Jack City came out.
    """
    age relativedelta(p..(movie.release_date), p..(actor.born.years
    r.. RETURN_FORMAT.f..(name=actor.name, movie=movie.title, age=age)
