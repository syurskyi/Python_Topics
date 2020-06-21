import argparse

#define ArgumentParser
parser = argparse.ArgumentParser(description='Example with long argument names')

#define long argument names
parser.add_argument('--noarg', action="store_true", default=False)
parser.add_argument('--string', action="store")
parser.add_argument('--integer', action="store", type=int)

#parse arguments
args = parser.parse_args()

#print arguments to screen
print ("noarg argument   : " + str(args.noarg))
print ("string argument  : " + str(args.string))
print ("integer argument : " + str(args.integer))