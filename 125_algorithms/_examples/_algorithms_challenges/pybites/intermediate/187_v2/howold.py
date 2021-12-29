from dataclasses import dataclass

import dateutil
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse


@dataclass
class Actor:
    name: str
    born: str


@dataclass
class Movie:
    title: str
    release_date: str


def get_age(actor: Actor, movie: Movie) -> str:
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} years old when {movie} came out.
       e.g.
       Wesley Snipes was 28 years old when New Jack City came out.
    """

    rd = relativedelta(parse(movie.release_date),parse(actor.born))
    year = rd.years

    return f"{actor.name} was {year} years old when {movie.title} came out."



