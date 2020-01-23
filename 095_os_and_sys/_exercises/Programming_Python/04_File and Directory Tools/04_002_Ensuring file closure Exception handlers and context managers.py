# myfile = open(filename, 'w')
# try:
#     ...process myfile...
# finally:
#     myfile.close()
#
# with open(filename, 'w') as myfile:
#     ...process myfile, auto-closed on statement exit...
#
# myfile = open(filename, 'w') # traditional form
# ...process myfile...
# myfile.close()
# with open(filename) as myfile: # context manager form
#     ...process myfile...
#
# with A() as a, B() as b:
#     ...statements...
#
# with A() as a:
#     with B() as b:
#         ...statements...
#
# with open('data') as fin, open('results', 'w') as fout:
#     for line in fin:
#         fout.write(transform(line))
