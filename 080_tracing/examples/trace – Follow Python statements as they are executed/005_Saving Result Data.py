# Counts and coverage information can be recorded as well, just as with the command line interface. The data must be
# saved explicitly, using the CoverageResults instance from the Trace object.

import trace
from trace_example.recurse import recurse

tracer = trace.Trace(count=True, trace=False)
tracer.runfunc(recurse, 2)

results = tracer.results()
results.write_results(coverdir='coverdir2')

# $ python trace_CoverageResults.py
#
# recurse(2)
# recurse(1)
# recurse(0)
#
# $ find coverdir2
#
# coverdir2
# coverdir2/trace_example.recurse.cover
# And the contents of coverdir2/trace_example.recurse.cover:
#
#        #!/usr/bin/env python
#        # encoding: utf-8
#        #
#        # Copyright (c) 2008 Doug Hellmann All rights reserved.
#        #
#        """
# >>>>>> """
#
#        #__version__ = "$Id$"
#        #end_pymotw_header
#
# >>>>>> def recurse(level):
#     3:     print 'recurse(%s)' % level
#     3:     if level:
#     2:         recurse(level-1)
#     3:     return
#
# >>>>>> def not_called():
# >>>>>>     print 'This function is never called.'

# To save the counts data for generating reports, use the infile and outfile argument to Trace.

import trace
from trace_example.recurse import recurse

tracer = trace.Trace(count=True, trace=False, outfile='trace_report.dat')
tracer.runfunc(recurse, 2)

report_tracer = trace.Trace(count=False, trace=False, infile='trace_report.dat')
results = tracer.results()
results.write_results(summary=True, coverdir='/tmp')

# Pass a filename to infile to read previously stored data, and a filename to outfile to write new results after tracing. If infile and outfile are the same, it has the effect of updating the file with cummulative data.
#
# $ python trace_report.py
#
# recurse(2)
# recurse(1)
# recurse(0)
# lines   cov%   module   (path)
#     8    50%   trace_example.recurse   (/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/trace/trace_example/recurse.py)