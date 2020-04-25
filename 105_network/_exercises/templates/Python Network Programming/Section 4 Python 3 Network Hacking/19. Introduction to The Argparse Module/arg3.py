# ______ a_p_
#
# #define ArgumentParser
# parser _ a_p_.A_P..
#
# #define argument names
# ?.a_a.. '-s' a.._'store', h.._'Store a simple value'
#
# ?.a_a.. '-c' a.._'store_const', c.._'value-to-store'
#                     h.._'Store a constant value'
#
# ?.a_a.. '-a' a.._'append', d.._ # list
#                     h.._'Add repeated values to a list'
#
# ?.a_a.. '-A' a.._'append_const', c.._'value-1-to-append'
#                     d.._ || d.._'const_collection',
#                     h.._'Add different values to list'
#
# ?.a_a.. '-B' a.._'append_const', c.._'value-2-to-append'
#                     d.._'const_collection',
#                     h.._'Add different values to list'
#
# ?.a_a.. '--version', a.._'version', v.._'%(prog)s 1.0'
#
# #parse arguments
# args _ ?.p_a..
#
# #print arguments to screen
# print ('simple_value     : ' + st. ?.s
# print ('constant_value   : ' + st. ?.c
# print ('collection       : ' + st. ?.a
# print ('const_collection : ' + st. ?.c_c..
# print ('version          : ' + st. ?.v..