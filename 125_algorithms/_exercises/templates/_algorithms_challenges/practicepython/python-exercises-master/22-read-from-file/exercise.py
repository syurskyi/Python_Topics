#! /Users/piotrjankiewicz/anaconda3/bin/python3.6
______ os

__ __name__ __ '__main__':
    cwd = os.getcwd()
    filePath = cwd + '/22-read-from-file/file.txt'
    namesCount = 0
    with open(filePath, 'r') as open_file:
        line = open_file.readline()
        w___ line:
            namesCount += 1
            line = open_file.readline()

    print('There are %s names in file.txt' % namesCount)
