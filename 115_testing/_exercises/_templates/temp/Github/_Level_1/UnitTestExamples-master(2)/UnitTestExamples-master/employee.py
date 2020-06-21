# Corey Schafer
# Python Tutorial: Unit Testing Your Code with the unittest Module
# https://www.youtube.com/watch?v=6tNS--WetLI

c_ Employee:
    """A sample Employee class"""

    raise_amt _ 1.05

    ___  -   first, last, pay
        first _ first
        last _ last
        pay _ pay

    @property
    ___ email
        r_ '{}.{}@email.com'.f..(first, last)

    @property
    ___ fullname
        r_ '{} {}'.f..(first, last)

    ___ apply_raise
        pay _ __.(pay * raise_amt)

    ___ monthly_schedule  month
        response _ requests.get(f'http://company.com/{last}/{month}')
        __ response.ok:
            r_ response.text
        ____:
            r_ 'Bad Response!'


