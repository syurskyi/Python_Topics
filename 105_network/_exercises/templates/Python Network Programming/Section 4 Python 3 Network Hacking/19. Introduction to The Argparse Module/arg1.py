______ a_p_

#define ArgumentParser
parser _ a_p_.A_P..(description_'Example argparse')

#define 1 character arguments
parser.a_a..('-a', action_"store_true", default_T..)
parser.a_a..('-b', action_"store")
parser.a_a..('-c', action_"store", type_int)

#parse arguments
args _ parser.parse_args

#print arguments to screen
print ("a argument : " + st.(args.a))
print ("b argument : " + st.(args.b))
print ("c argument : " + st.(args.c))