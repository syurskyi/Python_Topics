# # ch4/example1.py
#
# n_files _ 254
# files _    # list
#
# # method 1
# ___ i __ ra.. ?
#     ?.ap.. o.. 'output1/sample%i.txt'  ? _
#
# # method 2
# '''___ i __ range(n_files):
#     f = open('output1/sample%i.txt' % i, 'w')
#     files.append(f)
#     f.close()'''
#
# # method 3
# '''___ i __ range(n_files):
#     with open('output1/sample%i.txt' % i, 'w') as f:
#         files.append(f)'''
