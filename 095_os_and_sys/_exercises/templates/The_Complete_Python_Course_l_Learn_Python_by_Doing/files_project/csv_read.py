file _ o..('csv_data.txt', 'r')
lines _ file.readlines()
file.close()

lines _ [line.strip() ___ line __ lines[1:]]

___ line __ lines:
    person_data _ line.split(',')
    name _ person_data[0].title()
    age _ person_data[1]
    university _ person_data[2].title()
    degree _ person_data[3].capitalize()

    print(f'{name} is {age}, studying {degree} at {university}.')
