____ dataclasses _______ dataclass
____ dateutil.parser _______ parse
____ dateutil.relativedelta _______ relativedelta

RETURN_FORMAT = '{name} was {age} years old when {movie} came out.'


@dataclass
c_ Actor:
    name: s..
    born: s..


@dataclass
c_ Movie:
    title: s..
    release_date: s..


___ get_age(actor: Actor, movie: Movie) __ s..:
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} years old when {movie} came out.
       e.g.
       Wesley Snipes was 28 years old when New Jack City came out.
    """
    age = relativedelta(parse(movie.release_date), parse(actor.born)).years
    r.. RETURN_FORMAT.f..(name=actor.name, movie=movie.title, age=age)
