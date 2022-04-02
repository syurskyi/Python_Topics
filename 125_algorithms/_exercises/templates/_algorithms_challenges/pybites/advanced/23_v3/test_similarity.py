____ similarity _______ get_similarities


___ test_get_similarities
    # cast to list in case of generator
    similar_tags = l..(get_similarities

    # not interested in the order of the pairs
    similar_tags = {t..(s..(pair)) ___ pair __ similar_tags}

    expected = [('cheat sheet', 'cheat sheets'),
                ('python anywhere', 'pythonanywhere'),
                ('web scraping', 'webscraping'),
                ('object oriented', 'objectoriented'),
                ('web scraping', 'webscraping'),
                ('contextmanager', 'contextmanagers'),
                ('python anywhere', 'pythonanywhere'),
                ('contextmanager', 'contextmanagers'),
                ('magic methods', 'magicmethods'),
                ('magic methods', 'magicmethods'),
                ('code challenges', 'codechallenges'),
                ('cheat sheet', 'cheat sheets'),
                ('object oriented', 'objectoriented'),
                ('code challenges', 'codechallenges')]

    ___ hit __ expected:
        ... t..(s..(hit)) __ similar_tags, f'{hit} not in similar tags'