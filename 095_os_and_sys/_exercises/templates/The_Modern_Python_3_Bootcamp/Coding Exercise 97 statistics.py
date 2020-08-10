# Statistic Exercise Solution


___ statistics(file_name):
    w__ o..(file_name) __ file:
        lines _ file.readlines()

    r_ {"lines": le.(lines),
            "words": sum(le.(line.split(" ")) ___ line __ lines),
            "characters": sum(le.(line) ___ line __ lines)}