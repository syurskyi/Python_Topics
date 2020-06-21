# # this requires Python 3 to function properly
# ______ __ ___ __ a_p_
#
# #   This is a class designed to store the results from the parsed file until we're
# #   ready to print them out
# c_ modsecRec
#     #  this is the initializer
#     ___  -
#     	#  this is the list where all of the individual items are stored
#         storageList _   # list
#
#     #  append items to the list
#     ___ ap.. nI..
#         sL__.ap.. nI..
#
#     #  extract information from the message line and append it
#     ___ extractMessage msgLine
#         sL__.ap.. ?
#
# 	#  print the parsed data out to a file from the list
#     ___ printListToFile outputFilename
#         w__ o.. ? _ __ outHandle
#         	#  create a blank string
#             completeLine _ ''
#             ___ singleEntry __ sL__
#                 #  strip newlines out but append a comma for CSV format
#                 completeLine _ cL.. + sE__.rs.. + ","
#             #  now we can write the line out, but strip the trailing comma
#             oH__.w.. ?.rs.. ","
#
#     #  print out the entries to screen since we don't have an output file
#     ___ printList
#         ___ singleEntry __ sL__
#             print sE_.rs.. ","
#
# 	#  start over on the list since we've dumped one out
#     ___ clear
#         sL__ _   # list
#
#
# #  parse the command line arguments
# argParser _ a_p_.A_P..
# ?.a_a.. '-i', ty.._st. h.._'the input file with the ModSecurity audit log', re.._T..
# ?.a_a.. '-o', ty.._st. h.._'the output file this should generate')
# # argParser.add_argument('-f', type=str, help='the format of the output')
#
# p__sedArgs _ va.. ?.p_a..
#
# inputFileName _ pA.. 'i'
# outputFileName _ pA.. 'o'
#
# __ no. __.pa__.e.. iFN..
#     print("You must specify an input file that exists")
#     e..
#
# __ outputFileName an. __.pa__.e.. oFN..
#     __.r.. ?
#
# eachRecor. _ mR..
#
# w__ o.. iFN.. _ __ fH..
#     ___ dL.. __ fH..
#         __ '--' __ daL..
#             __ '-A--' __ dL..
#                 dateInfo _ fH__.r_l..
#                 logDate _ dI.. dI__.f.. "[" +1;dI__.f.. ":"
#                 logTime _ dI.. dI__.f.. ":" +1;dI__.f.. " "
#                 eR__.ap.. lD..
#                 eR__.ap.. lT..
#             __ '-B--' __ dL..
#                 httpReq _ fH__.rl..
#                 eR__.ap.. hR..
#             __ '-H--' __ dL..
#                 # loop until we get to the end
#                 ___ mL.. __ fH__
#                     __ 'Message' __ mL..
#                         eR__.eM.. ?
#                     ____
#                         b..
#             __ '-Z--' __ dL..
#                 # do something with all the data we have acquired
#                 __ oFN..
#                 	eR__.pLTF.. ?
#                 ____
#                 	eR__.pL..
#                 eR__.c..
#
#
# fH__.c..
