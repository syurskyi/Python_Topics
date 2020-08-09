#! /Users/piotrjankiewicz/anaconda3/bin/python3.6
______ os

___ fileToArray(filePath
    with open(filePath, 'r') as file:
        lines = []
        line = file.readline()
        w___ line:
            __ line != '':
                lines.append(line.rstrip())
                line = file.readline()
        r_ lines



__ __name__ __ '__main__':
    cwd = os.getcwd()
    prime = cwd + '/23-file-overlap/prime.txt'
    happy = cwd + '/23-file-overlap/happy.txt'

    primes = fileToArray(prime)
    happies = fileToArray(happy)

    print('Primes: ' + str(primes) + '\n\nHappies: ' + str(happies))

    print('\n\nIntersection of both files are: '+ str(set(primes).intersection(happies)))