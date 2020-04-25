______ a_p_

#define ArgumentParser
parser _ a_p_.A_P..(description_'Example with long argument names')

#define long argument names
parser.a_a..('--noarg', action_"store_true", default_False)
parser.a_a..('--string', action_"store")
parser.a_a..('--integer', action_"store", type_int)

#parse arguments
args _ parser.parse_args

#print arguments to screen
print ("noarg argument   : " + st.(args.noarg))
print ("string argument  : " + st.(args.string))
print ("integer argument : " + st.(args.integer))