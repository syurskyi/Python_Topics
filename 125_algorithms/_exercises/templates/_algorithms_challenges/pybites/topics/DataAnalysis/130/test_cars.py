____ cars _______ most_prolific_automaker, get_models


___ test_most_prolific_automaker_1999
    ... most_prolific_automaker(1999) __ 'Dodge'


___ test_most_prolific_automaker_2008
    ... most_prolific_automaker(2008) __ 'Toyota'


___ test_most_prolific_automaker_2013
    ... most_prolific_automaker(2013) __ 'Hyundai'


___ test_get_models_volkswagen
    models = get_models('Volkswagen', 2008)
    # sets are unordered
    ... l..(models) __ 2
    ... 'Jetta' __ models
    ... 'Rabbit' __ models


___ test_get_models_nissan
    ... get_models('Nissan', 2000) __ {'Pathfinder'}


___ test_get_models_open
    # not in data set
    ... get_models('Opel', 2008) __ s..()

___ test_get_models_mercedes
    models = get_models('Mercedes-Benz', 2007)
    ... l..(models) __ 3
    ... 'SL-Class' __ models
    ... 'GL-Class' __ models
    ... 'CL-Class' __ models