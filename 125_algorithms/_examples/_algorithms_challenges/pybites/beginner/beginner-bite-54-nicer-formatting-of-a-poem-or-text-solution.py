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


def print_hanging_indents(poem):
  #  poem = poem.strip()
    whitespace = " "
    prefix = INDENTS*whitespace
    current_line_cnt = 0
    target_poem = []
    for line in poem.splitlines():
        # trim current line
        current_line = line.lstrip()
        # adjust counters
        if line == "":
            current_line_cnt = 0
            continue
        else:
            current_line_cnt += 1
        # check the line we're dealing with
        if current_line_cnt == 0:
            line_to_be_inserted = ""
        elif current_line_cnt == 1:
            line_to_be_inserted = current_line
        elif current_line_cnt > 1:
            line_to_be_inserted = prefix + current_line
        target_poem.append(line_to_be_inserted)
    result = '\n'.join(target_poem)
    print(result)




print_hanging_indents(shakespeare_unformatted)
print_hanging_indents(rosetti_unformatted)

