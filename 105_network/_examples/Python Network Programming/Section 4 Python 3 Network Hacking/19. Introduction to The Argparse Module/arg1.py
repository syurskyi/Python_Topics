import argparse

#define ArgumentParser
parser = argparse.ArgumentParser(description='Example argparse')

#define 1 character arguments
parser.add_argument('-a', action="store_true", default=True)
parser.add_argument('-b', action="store")
parser.add_argument('-c', action="store", type=int)

#parse arguments
args = parser.parse_args()

#print arguments to screen
print ("a argument : " + str(args.a))
print ("b argument : " + str(args.b))
print ("c argument : " + str(args.c))