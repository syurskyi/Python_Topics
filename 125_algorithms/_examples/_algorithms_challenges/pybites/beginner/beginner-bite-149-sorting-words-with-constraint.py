"""
Here is a list of words Jacob is trying to sort:

>>> words = "It's almost Holidays and PyBites wishes You a Merry Christmas and a Happy 2019".split()
>>> sorted(words)

['2019', 'Christmas', 'Happy', 'Holidays', "It's", 'Merry', 'PyBites', 'You', 'a', 'a', 'almost', 'and', 'and', 'wishes']
Hmm ... that year goes first. He actually wants words starting with a digit (first character) to go last!

Could you complete the function below to do this for him? So the result would be:

['a', 'a', 'almost', 'and', 'and', 'Christmas', 'Happy', 'Holidays', "It's", 'Merry', 'PyBites', 'wishes', 'You', '2019']
By the way, you can submit ideas/needs/wishes for Bites here. Cheers!

See you in the next Bite and keep calm and code in Python!
"""
words = "Let's see how4 this 1sorts, hope it works 4 this B1te 22 55abc abc55".split()

def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    # New list for numbers
    nums = []
    print(f"### Initial list {words}")
    ### IMPORTANT!!!! DO NOT modify a list when iterating over it!!!!
    for word in words:
        if word[0].isdigit():
            nums.append(word)
    nums = sorted(nums)
    for num in nums:
        words.remove(num)

    s = sorted(words, key=lambda s: s.casefold())
    print(s)
    print(nums)
    for num in nums:
        s.append(num)
    print(s)
    return s


sort_words_case_insensitively(words)

