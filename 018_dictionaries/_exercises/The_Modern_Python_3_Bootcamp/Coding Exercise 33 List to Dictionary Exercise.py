# # There are many potential solutions for this:
# #
# # Using a dictionary comprehension
#
# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# answer = thing 0 ; thing 1 ___ ? __ ?
#
# # An alternate solution using a dict comprehension, without any references to list indexes:
#
# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# answer = k v ___ ? ? __ ?
#
# # Finally, a really simple solution.
# # If you have a list of pairs, you can very easily turn it into a dictionary using dict()
#
# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# answer = dict(person)
