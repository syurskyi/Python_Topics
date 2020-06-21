'''
gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
'''


def yes_or_no():
    pass

# Yes Or No Generator Solution
#
# yes_or_no  loops forever (while True) and yields answer , and then toggles answer from yes to no, or vice versa.


def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"
