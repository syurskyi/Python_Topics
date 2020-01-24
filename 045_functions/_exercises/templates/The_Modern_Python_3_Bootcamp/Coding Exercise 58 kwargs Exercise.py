# combine_words solution
#
#     I check if kwargs contains "prefix".
#         If it does, I return the value of prefix + the word
#     Otherwise, I check to see if "suffix" was provided as a kwarg
#         If it was, I return the word followed by the value of suffix
#     Otherwise, I just return the word on its own.


def combine_words(word, **kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word

