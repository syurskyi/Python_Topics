______ a_p_

#define ArgumentParser
parser _ a_p_.A_P..

#define argument names
parser.a_a..('-s', action_'store', help_'Store a simple value')

parser.a_a..('-c', action_'store_const', const_'value-to-store',
                    help_'Store a constant value')

parser.a_a..('-a', action_'append', default_[],
                    help_'Add repeated values to a list',)

parser.a_a..('-A', action_'append_const', const_'value-1-to-append',
                    default_[], dest_'const_collection',
                    help_'Add different values to list')

parser.a_a..('-B', action_'append_const', const_'value-2-to-append',
                    dest_'const_collection',
                    help_'Add different values to list')

parser.a_a..('--version', action_'version', version_'%(prog)s 1.0')

#parse arguments
args _ parser.parse_args

#print arguments to screen
print ('simple_value     : ' + st.(args.s))
print ('constant_value   : ' + st.(args.c))
print ('collection       : ' + st.(args.a))
print ('const_collection : ' + st.(args.const_collection))
print ('version          : ' + st.(args.version))