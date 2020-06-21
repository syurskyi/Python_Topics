# Using list comprehensions:

answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
answer2 = [val for val in [1, 2, 3, 4, 5, 6] if val % 2 == 0]

# Using good old manual loops:

answer = []
for person in ["Elie", "Tim", "Matt"]:
    answer.append(person[0])

answer2 = []
for num in [1, 2, 3, 4, 5, 6]:
    if num % 2 == 0:
        answer2.append(num)
