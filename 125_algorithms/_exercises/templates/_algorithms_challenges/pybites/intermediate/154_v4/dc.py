____ dataclasses _______ dataclass, field

@dataclass(order=T..)
c_ Bite
    number: i.. = field(compare=T..)
    title: s..
    level: s.. = 'Beginner'

    ___ __post_init__
        title = title.capitalize()