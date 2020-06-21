"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter,
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags
"""

______ fileinput
______ re

___ convertStrong(line
  line _ re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line _ re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  r_ line

___ convertEm(line
  line _ re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line _ re.sub(r'_(.*)_', r'<em>\1</em>', line)
  r_ line

___ line __ fileinput.__..(
  line _ line.rstrip()
  line _ convertStrong(line)
  line _ convertEm(line)
  print('<p>' + line + '</p>',)