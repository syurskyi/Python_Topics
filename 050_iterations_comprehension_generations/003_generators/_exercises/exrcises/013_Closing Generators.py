# # Closing Generators
# # We can actually close a generator by sending it a special message, calling its close ()  method.
#
# import csv
#
# ___ parse_file f_name
#     print 'opening file...'
#     f _ op.. f_name, 'r'
#     t..
#         dialect _ csv.Sni...  .sniff f.read 2000
#         f.se.. 0
#         ne.. f   # skip header row
#         reader _ csv.re.. f, dialect_dialect
#         ___ row i_ reader
#             t..
#                 y____ row
#             e_____ G..E..
#                 print 'got a close...'
#                 r...
#     f___
#         print 'cleaning up...'
#         f.cl..
#
# parser _ parse_file 'cars.csv'
# ___ row i_ it__t__.isl... parser 5
#     print r..
#
# pa__.cl..
#
# # Closing Generators
# #
# # We can actually close a generator by sending it a special message, calling its close   method.
#
# ___ parse_file f_name :
#     print 'opening file...'
#     f _ op.. f_name 'r'
#     t..:
#         dialect _ csv.Sn...  .sniff f.read 2000
#         f.se.. 0
#         ne.. f   # skip header row
#         reader _ csv.re.. f dialect_dialect
#         ___ row i_ reader
#             t..
#                 y____ row
#             e_____ G..E..
#                 print 'got a close...'
#                 r_
#     f___:
#         print 'cleaning up...'
#         f.cl..
#
# parser _ parse_file 'cars.csv'
# ___ row i_ it__t__.isl... parser 5
#     print row
#
# pa_cl..
#
# # Closing Generators
# # ___ save_to_db
# # Notice how we're not even catching the GeneratorExit exception - we really don't need to -
# # that exception will be raised, the f___ block will run, and the GeneratorExit exception will be bubbled up to
# # Python who will expect it after the call to close
#
# ___ save_to_db
#     print 'starting new transaction'
#     is_abort _ Fa..
#     t..
#         w___ T
#             data _ y____
#             print 'sending data to database:', ev.. d..
#     e_____ E...
#         is_abort _ T..
#         r...
#     f___:
#         i_ is_abort:
#             print 'aborting transaction'
#         e___
#             print 'committing transaction'
#
# trans _ save_to_db
# ne.. trans
# trans.send '1 + 1'
# trans.close
#
# trans _ save_to_db
# ne.. trans
# trans.send '1 / 0'
