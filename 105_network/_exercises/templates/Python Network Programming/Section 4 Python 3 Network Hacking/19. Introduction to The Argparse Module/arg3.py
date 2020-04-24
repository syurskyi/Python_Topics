import argparse

#define ArgumentParser
parser = argparse.ArgumentParser()

#define argument names
parser.add_argument('-s', action='store', help='Store a simple value')

parser.add_argument('-c', action='store_const', const='value-to-store',
                    help='Store a constant value')

parser.add_argument('-a', action='append', default=[],
                    help='Add repeated values to a list',)

parser.add_argument('-A', action='append_const', const='value-1-to-append',
                    default=[], dest='const_collection',
                    help='Add different values to list')

parser.add_argument('-B', action='append_const', const='value-2-to-append',
                    dest='const_collection',
                    help='Add different values to list')

parser.add_argument('--version', action='version', version='%(prog)s 1.0')

#parse arguments
args = parser.parse_args()

#print arguments to screen
print ('simple_value     : ' + str(args.s))
print ('constant_value   : ' + str(args.c))
print ('collection       : ' + str(args.a))
print ('const_collection : ' + str(args.const_collection))
print ('version          : ' + str(args.version))