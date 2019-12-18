# Another similarity with % expressions is that you can achieve more specific layouts by
# adding extra syntax in the format string. For the formatting method, we use a colon
# after the possibly empty substitution target’s identification, followed by a format specifier
# that can name the field size, justification, and a specific type code. Here’s the formal
# structure of what can appear as a substitution target in a format string—its four parts
# are all optional, and must appear without intervening spaces:
# {fieldname component !conversionflag :formatspec}
# In this substitution target syntax:
# • fieldname is an optional number or keyword identifying an argument, which may
# be omitted to use relative argument numbering in 2.7, 3.1, and later.
# • component is a string of zero or more “.name” or “[index]” references used to fetch
# attributes and indexed values of the argument, which may be omitted to use the
# whole argument value.
# • conversionflag starts with a ! if present, which is followed by r, s, or a to call repr,
# str, or ascii built-in functions on the value, respectively.
# • formatspec starts with a : if present, which is followed by text that specifies how
# the value should be presented, including details such as field width, alignment,
# padding, decimal precision, and so on, and ends with an optional data type code.
#
# The
# formatspec
# component
# after
# the
# colon
# character
# has
# a
# rich
# format
# all
# its
# own, and
# is formally
# described as follows(brackets
# denote
# optional
# components and are
# not
# coded
# literally):
# [[fill]align][sign][  # ][0][width][,][.precision][typecode]
#     In
# this, fill
# can
# be
# any
# fill
# character
# other
# than
# { or}; align
# may
# be <, >, =, or ^, for
# left alignment, right alignment, padding after a sign character, or centered alignment,
# respectively; sign may be +, −, or space; and the, (comma) option requests a comma
# for a thousands separator as of Python 2.7 and 3.1.width and precision are much as
# in the % expression, and the formatspec may also contain nested {} format strings with
# field names only, to take values from the arguments list dynamically (much like the *
# in formatting expressions).
# The method’s typecode options almost completely overlap with those used in % expressions
# and listed previously in Table 7-4, but the format method also allows a b type
# code used to display integers in binary format (it’s equivalent to using the bin built- in
# call), allows a % type code to display percentages, and uses only d for base-10 integers
# (i or u are not used here).Note that unlike the expression’s % s, the s type code here
# requires a string object argument; omit the type code to accept any type generically.
# See Python’s library manual for more on substitution syntax that we’ll omit here.In
# addition to the string’s format method, a single object may also be formatted with the
# format(object, formatspec) built- in function (which the method uses internally), and
# may be customized in user-defined classes with the __format__ operator-overloading
# method (see Part VI).