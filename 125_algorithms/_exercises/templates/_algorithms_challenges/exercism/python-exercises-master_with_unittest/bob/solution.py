___ hey(stimulus
    stimulus = stimulus.s..

    __ _is_silence(stimulus
        r.. 'Fine. Be that way!'
    ____ _is_shouting(stimulus
        r.. 'Whoa, chill out!'
    ____ _is_question(stimulus
        r.. 'Sure.'
    ____:
        r.. 'Whatever.'


___ _is_silence(stimulus
    r.. stimulus __ ''


___ _is_shouting(stimulus
    r.. stimulus.isupper()


___ _is_question(stimulus
    r.. stimulus.e.. '?')
