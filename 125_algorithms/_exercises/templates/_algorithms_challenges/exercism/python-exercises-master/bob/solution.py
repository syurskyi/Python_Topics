___ hey(stimulus
    stimulus = stimulus.strip()

    __ _is_silence(stimulus
        r_ 'Fine. Be that way!'
    ____ _is_shouting(stimulus
        r_ 'Whoa, chill out!'
    ____ _is_question(stimulus
        r_ 'Sure.'
    ____
        r_ 'Whatever.'


___ _is_silence(stimulus
    r_ stimulus __ ''


___ _is_shouting(stimulus
    r_ stimulus.isupper()


___ _is_question(stimulus
    r_ stimulus.endswith('?')
