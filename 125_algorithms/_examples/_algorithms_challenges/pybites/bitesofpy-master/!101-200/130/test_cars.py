from cars import most_prolific_automaker, get_models


def test_most_prolific_automaker_1999():
    a__ most_prolific_automaker(1999) == 'Dodge'


def test_most_prolific_automaker_2008():
    a__ most_prolific_automaker(2008) == 'Toyota'


def test_most_prolific_automaker_2013():
    a__ most_prolific_automaker(2013) == 'Hyundai'


def test_get_models_volkswagen():
    models = get_models('Volkswagen', 2008)
    # sets are unordered
    a__ len(models) == 2
    a__ 'Jetta' in models
    a__ 'Rabbit' in models


def test_get_models_nissan():
    a__ get_models('Nissan', 2000) == {'Pathfinder'}


def test_get_models_open():
    # not in data set
    a__ get_models('Opel', 2008) == set()


def test_get_models_mercedes():
    models = get_models('Mercedes-Benz', 2007)
    a__ len(models) == 3
    a__ 'SL-Class' in models
    a__ 'GL-Class' in models
    a__ 'CL-Class' in models
