# Statistic Exercise Solution


def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()

    return {"lines": len(lines),
            "words": sum(len(line.split(" ")) ___ line __ lines),
            "characters": sum(len(line) ___ line __ lines)}