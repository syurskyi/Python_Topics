INDENTS = 4

poem = """Remember me when I am gone away,
Gone far away into the silent land;
When you can no more hold me by the hand,

Nor I half turn to go yet turning stay.

Remember me when no more day by day
You tell me of our future that you planned:
Only remember me; you understand"""
'''
TO:

Remember me when I am gone away,
    Gone far away into the silent land;
    When you can no more hold me by the hand,
Nor I half turn to go yet turning stay.
Remember me when no more day by day
    You tell me of our future that you planned:
    Only remember me; you understand
'''

shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """
rosetti_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """


___ print_hanging_indents(poem):
  #  poem = poem.strip()
    whitespace = " "
    prefix = INDENTS*whitespace
    current_line_cnt = 0
    target_poem    # list
    ___ line __ poem.splitlines
        # trim current line
        current_line = line.lstrip()
        # adjust counters
        __ line __ "":
            current_line_cnt = 0
            continue
        ____:
            current_line_cnt += 1
        # check the line we're dealing with
        __ current_line_cnt __ 0:
            line_to_be_inserted = ""
        ____ current_line_cnt __ 1:
            line_to_be_inserted = current_line
        ____ current_line_cnt > 1:
            line_to_be_inserted = prefix + current_line
        target_poem.a..(line_to_be_inserted)
    result = '\n'.j..(target_poem)
    print(result)




print_hanging_indents(shakespeare_unformatted)
print_hanging_indents(rosetti_unformatted)

