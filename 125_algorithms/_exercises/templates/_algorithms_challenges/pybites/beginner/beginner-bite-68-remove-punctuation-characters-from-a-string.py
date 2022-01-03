'''
Complete remove_punctuation which receives an input string and strips out all
punctuation characters (!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~).

Return the resulting string. You can go full loop, list comprehension or maybe some nice stdlib functionality?
'''

_______ string

___ remove_punctuation_solution_1(input_string):
    """Return a str with punctuation chars stripped out"""
    new_str    # list
    ___ c __ input_string:
        __ c __ string.punctuation:
            continue
        new_str.a..(c)
    out = ''.j..(new_str)
    print(out)

___ remove_punctuation_solution_2(input_string):
    """Return a str with punctuation chards stripped out"""
    new_list = [i ___ i __ input_string __ i n.. __ string.punctuation]
    out = ''.j..(new_list)
    r.. out

___ remove_punctuation_solution_3(input_string):
     # dict_variable = {key:value for (key,value) in dictonary.items()}
     # https://www.datacamp.com/community/tutorials/python-dictionary-comprehension
     d = {key: N.. ___ key __ string.punctuation}
     print(d)



#remove_punctuation_solution_1("test1234!()vtpqaz")

print(remove_punctuation_solution_2("test1234!()vtpqaz"))

remove_punctuation_solution_3("test123")