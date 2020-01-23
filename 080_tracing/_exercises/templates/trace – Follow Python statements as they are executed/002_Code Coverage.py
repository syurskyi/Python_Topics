# Code Coverage
# Running trace from the command line with the --count option will produce code coverage report information,
# so you can see which lines are run and which are skipped. Since your program is usually made up of multiple files,
# a separate coverage report is produced for each. By default the coverage report files are written to
# the same directory as the module, named after the module but with a .cover extension instead of .py.
#
# $ python -m trace --count trace_example/main.py
#
# This is the main program.
# recurse(2)
# recurse(1)
# recurse(0)
# And two output files, trace_example/main.cover:
#
#
#     1: from recurse import recurse
#
#     1: def main():
#     1:     print 'This is the main program.'
#     1:     recurse(2)
#     1:     return
#
#     1: if __name__ == '__main__':
#     1:     main()
# and trace_example/recurse.cover:
#
#
#     1: def recurse(level):
#     3:     print 'recurse(%s)' % level
#     3:     if level:
#     2:         recurse(level-1)
#     3:     return
#
#     1: def not_called():
#            print 'This function is never called.'
# Note Although the line def recurse(level): has a count of 1, that does not mean the function was only run once.
# It means the function definition was only executed once.
# It is also possible to run the program several times, perhaps with different options, to save the coverage data
# and produce a combined report.
#
# $ python -m trace --coverdir coverdir1 --count --file coverdir1/coverage\
# _report.dat trace_example/main.py
#
# Skipping counts file 'coverdir1/coverage_report.dat': [Errno 2] No such file or directory:
# 'coverdir1/coverage_report.dat'
# This is the main program.
# recurse(2)
# recurse(1)
# recurse(0)
#
# $ python -m trace --coverdir coverdir1 --count --file coverdir1/coverage\
# _report.dat trace_example/main.py
#
# This is the main program.
# recurse(2)
# recurse(1)
# recurse(0)
#
# $ python -m trace --coverdir coverdir1 --count --file coverdir1/coverage\
# _report.dat trace_example/main.py
#
# This is the main program.
# recurse(2)
# recurse(1)
# recurse(0)
# Once the coverage information is recorded to the .cover files, you can produce reports with the --report option.
#
# $ python -m trace --coverdir coverdir1 --report --summary --missing --fi\
# le coverdir1/coverage_report.dat trace_example/main.py
#
# lines   cov%   module   (path)
#   515     0%   trace   (/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/trace.py)
#     8   100%   trace_example.main   (trace_example/main.py)
#     8    87%   trace_example.recurse   (trace_example/recurse.py)
# Since the program ran three times, the coverage report shows values three times higher than the first report.
# The --summary option adds the percent covered information to the output above. The recurse module is only 87% covered.
# A quick look at the cover file for recurse shows that the body of not_called() is indeed never run, indicated
# by the >>>>>> prefix.
#
#
#     3: def recurse(level):
#     9:     print 'recurse(%s)' % level
#     9:     if level:
#     6:         recurse(level-1)
#     9:     return
#
#     3: def not_called():
# >>>>>>     print 'This function is never called.'