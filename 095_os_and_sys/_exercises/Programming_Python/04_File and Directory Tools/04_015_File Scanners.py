# C:\...\PP4E\System\Filetools> python commands.py hillbillies.txt
# Ms. Granny
# Mr. Jethro
# Ms. Elly May
# Mr. "Uncle Jed"

commands = {'*': 'Ms.', '+': 'Mr.'} # data is easier to expand than code?
def processLine(line):
    try:
        print(commands[line[0]], line[1:-1])
    except KeyError:
        raise UnknownCommand(line)

def scanner(name, function):
    list(map(function, open(name, 'r')))

def scanner(name, function):
    [function(line) for line in open(name, 'r')]

def scanner(name, function):
    list(function(line) for line in open(name, 'r'))