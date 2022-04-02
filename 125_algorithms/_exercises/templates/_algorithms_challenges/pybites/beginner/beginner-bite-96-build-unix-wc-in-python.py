'''
In this Bite you will convert Unix' wc command into Python. Your function takes a file (absolute path),
reads it in and calculates the lines/words/chars. It returns a string of these numbers and the filename,
like as a typical wc output, for example:

$ wc wc.py
      13      56     514 wc.py
Don't worry about the amount of white space between the columns, you can use tabs or spaces.

Unix files add an extra newline to the end, you don't have to make that assumption here, so 'Hello\nworld' == 11 chars
not 12 as Unix' wc would return. Let's keep it simple. Do note that newline (\n) counts as a char.

See the tests for more info. Thanks Brian for introducing us to pytest's tmp_path fixture!

Have fun and keep coding in Python!

'''

___ wc(file_
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    cnt_line = 0
    cnt_words = 0
    cnt_chars = 0
    within_word = F..
    ___
        fo = o.. file_, _
    ______:
        print("Cannot open file")
    filename = fo.name
    ___ line __ fo:
        cnt_line += 1
        cnt_chars += l..(line)
        ___ c __ line:
            __ c != ' ' a.. c != '\n' a.. c != '\t':
                within_word = T..
                _____
            __ within_word __ T.. a.. (c __ ' ' o. c __ '\t' o. c __ '\n'
                cnt_words += 1
                within_word = F..
    fo.c..

    print _*{cnt_line} {cnt_words} {cnt_chars} {filename}')


wc('beginner-bite-96-test-file.txt')