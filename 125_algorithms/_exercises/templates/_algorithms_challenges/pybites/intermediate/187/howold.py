____ dataclasses _______ dataclass
____ dateutil _______ parser
____ dateutil.relativedelta _______ relativedelta


@dataclass
c_ Actor:
    name: s..
    born: s..


@dataclass
c_ Movie:
    title: s..
    release_date: s..


___ get_age(actor: Actor, movie: Movie) -> s..:
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} years old when {movie} came out.
       e.g.
       Wesley Snipes was 28 years old when New Jack City came out.
    """
    date_delta = relativedelta(parser.parse(movie.release_date), parser.parse(actor.born))
    r.. f"{actor.name} was {date_delta.years} years old when {movie.title} came out."


# if __name__ == "__main__":
#     print(get_age(Actor('Wesley Snipes', 'July 31, 1962'), Movie('New Jack City', 'January 17, 1991')))
