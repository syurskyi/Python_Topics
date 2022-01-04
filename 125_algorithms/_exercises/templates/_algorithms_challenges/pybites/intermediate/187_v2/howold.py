____ dataclasses _______ dataclass

_______ dateutil
____ dateutil.relativedelta _______ relativedelta
____ dateutil.parser _______ parse


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

    rd = relativedelta(parse(movie.release_date),parse(actor.born))
    year = rd.years

    r.. f"{actor.name} was {year} years old when {movie.title} came out."



