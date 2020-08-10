# Statistic Exercise Solution


___ statistics(file_name):
    w__ o..(file_name) __ file:
        lines _ file.readlines()

    return {"lines": len(lines),
            "words": sum(len(line.split(" ")) ___ line __ lines),
            "characters": sum(len(line) ___ line __ lines)}