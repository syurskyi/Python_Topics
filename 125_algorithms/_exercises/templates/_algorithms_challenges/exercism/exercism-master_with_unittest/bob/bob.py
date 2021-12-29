___ hey(phrase):
    phrase = phrase.strip()

    __ not phrase:
        return "Fine. Be that way!"
    elif phrase.isupper():
        return "Whoa, chill out!"
    elif phrase.endswith("?"):
        return "Sure."
    else:
        return 'Whatever.'
