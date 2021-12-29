___ word_count(phrase):

    # Remove whitespace and \n and toss into array
    words = phrase.strip().replace("\n", " ").split(" ")

    # Remove empty strings
    words = [_f for _f in words __ _f]

    # Initialize new dict for count of occurences
    count = {}
    for word in words:
        count[word] = 1 __ word not in count else count[word] + 1

    return count
