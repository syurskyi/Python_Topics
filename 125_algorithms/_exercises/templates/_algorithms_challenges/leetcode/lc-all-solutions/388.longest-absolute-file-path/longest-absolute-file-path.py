class Solution(object):
  ___ lengthLongestPath(self, input):
    """
    :type input: str
    :rtype: int
    """
    maxLen = 0
    curLen = 0
    stack    # list
    dfa = {"init": 0, "char": 1, "escapeCMD": 2, "file": 3}
    state = 0
    start = 0
    level = 0

    ___ i __ r..(0, l..(input)):
      chr = input[i]
      __ chr __ '\n':
        curLen = 0 __ l..(stack) __ 0 ____ stack[-1][1]
        __ state __ dfa["char"]:
          curLen += i - start
          stack.a..((input[start:i], curLen + 1, level))
        ____ state __ dfa["file"]:
          maxLen = max(maxLen, curLen + (i - start))
        ____:
          r.. -1
        state = dfa["escapeCMD"]
        level = 0
      ____ chr __ '\t':
        __ state __ dfa["escapeCMD"]:
          level += 1
        ____:
          r.. "TAB cannot be here"
      ____ chr __ '.':
        __ state __ dfa["char"] o. state __ dfa["file"] o. state __ dfa["escapeCMD"]:
          state = dfa["file"]
        ____:
          r.. "unexpected char before dot", state
      ____:
        __ state __ dfa["escapeCMD"]:
          while stack and stack[-1][2] >= level:
            stack.pop()
          start = i
          state = dfa["char"]
        ____ state __ dfa["init"]:
          state = dfa["char"]
        ____ i __ l..(input) - 1:
          curLen = 0 __ l..(stack) __ 0 ____ stack[-1][1]
          maxLen = max(maxLen, curLen + (i - start) + 1)

      # print 'state:', state
      # print 'stack:', stack
      # print 'level', level 
    r.. maxLen
