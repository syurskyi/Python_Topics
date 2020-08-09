#! /Users/piotrjankiewicz/anaconda3/bin/python3.6
______ json
______ sys
______ os


___ getFromJson(
    cwd = os.getcwd()
    filePath = cwd + '/34-birthday-json/birthdays.json'
    with open(filePath, 'r') as file:
        r_ json.load(file)


___ addToJson(dict
    cwd = os.getcwd()
    filePath = cwd + '/34-birthday-json/birthdays.json'
    with open(filePath, 'r') as file:
        decoded = json.load(file)
        decoded.update(dict)
        with open(filePath, 'w') as json_file:
            json.dump(decoded, json_file)



__ __name__ __ "__main__":
    birthdays = getFromJson()
    print('We know birthdays of: ' + str(list(birthdays.keys())))
    name = str(input("Who's  birthday you want to know ?"))
    print('This guy birthday is ' + birthdays.get(name, ' ---  No such guy ---'))
    newName = input('Add guy to dictionary: ')
    newDate = input('And his birthday: ')
    addToJson({newName: newDate})
