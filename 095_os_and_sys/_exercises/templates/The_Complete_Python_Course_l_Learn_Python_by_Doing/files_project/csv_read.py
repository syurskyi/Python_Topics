file = o..('csv_data.txt', 'r')
lines = file.readlines()
file.close()

lines = [line.strip() ___ line __ lines[1:]]

___ line __ lines:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].title()
    degree = person_data[3].capitalize()

    print(f'{name} is {age}, studying {degree} at {university}.')
