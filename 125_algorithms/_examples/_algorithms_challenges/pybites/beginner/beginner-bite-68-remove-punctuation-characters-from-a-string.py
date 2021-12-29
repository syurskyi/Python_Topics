'''
Complete remove_punctuation which receives an input string and strips out all
punctuation characters (!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~).

Return the resulting string. You can go full loop, list comprehension or maybe some nice stdlib functionality?
'''

import string

def remove_punctuation_solution_1(input_string):
    """Return a str with punctuation chars stripped out"""
    new_str = []
    for c in input_string:
        if c in string.punctuation:
            continue
        new_str.append(c)
    out = ''.join(new_str)
    print(out)

def remove_punctuation_solution_2(input_string):
    """Return a str with punctuation chards stripped out"""
    new_list = [i for i in input_string if i not in string.punctuation]
    out = ''.join(new_list)
    return out

def remove_punctuation_solution_3(input_string):
     # dict_variable = {key:value for (key,value) in dictonary.items()}
     # https://www.datacamp.com/community/tutorials/python-dictionary-comprehension
     d = {key: None for key in string.punctuation}
     print(d)



#remove_punctuation_solution_1("test1234!()vtpqaz")

print(remove_punctuation_solution_2("test1234!()vtpqaz"))

remove_punctuation_solution_3("test123")