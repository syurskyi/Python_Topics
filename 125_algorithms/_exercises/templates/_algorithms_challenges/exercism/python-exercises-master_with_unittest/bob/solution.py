___ hey(stimulus):
    stimulus = stimulus.strip()

    __ _is_silence(stimulus):
        return 'Fine. Be that way!'
    elif _is_shouting(stimulus):
        return 'Whoa, chill out!'
    elif _is_question(stimulus):
        return 'Sure.'
    else:
        return 'Whatever.'


___ _is_silence(stimulus):
    return stimulus == ''


___ _is_shouting(stimulus):
    return stimulus.isupper()


___ _is_question(stimulus):
    return stimulus.endswith('?')
