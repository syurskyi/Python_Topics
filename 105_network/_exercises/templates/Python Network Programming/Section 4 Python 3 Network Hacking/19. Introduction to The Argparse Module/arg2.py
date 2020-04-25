______ a_p_

#define ArgumentParser
parser _ a_p_.A_P..(d.._'Example with long argument names')

#define long argument names
?.a_a..('--noarg', action_"store_true", default_False)
?.a_a..('--string', action_"store")
?.a_a..('--integer', action_"store", type_int)

#parse arguments
args _ ?.parse_args

#print arguments to screen
print ("noarg argument   : " + st.(args.noarg))
print ("string argument  : " + st.(args.string))
print ("integer argument : " + st.(args.integer))