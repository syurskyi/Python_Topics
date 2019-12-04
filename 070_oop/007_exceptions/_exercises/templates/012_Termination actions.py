# Termination actions
def fetcher(obj, index):
    return obj[index]

x = 'spam'
print('#' * 52 + ' Termination actions')
try:
    fetcher(x, 3)
finally:                              # Termination actions
    print('after fetch')

fetcher(x, 3)

def after():
    try:
        fetcher(x, 3)
    finally:
        print('after fetch')
    print('after try?')

after()
#
with open('lumberjack.txt', 'w') as file:        # Always close file on exit
    file.write('The newest test!\n')