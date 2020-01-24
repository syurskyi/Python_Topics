# Using list comprehensions(the more Pythonic way):

answer = [val for val in [1, 2, 3, 4] if val in [3, 4, 5, 6]]
# the slice [::-1] is a quick way to reverse a string
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]

# Without list comprehensions, things are a bit longer:

answer = []
for x in [1,2,3,4]:
    if x in [3,4,5,6]:
        answer.append(x)
answer2 = []
for name in ["Elie", "Tim", "Matt"]:
    answer2.append(name[::-1].lower())
