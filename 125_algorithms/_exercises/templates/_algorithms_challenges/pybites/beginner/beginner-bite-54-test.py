_______ pytest
_______ pluggy
_______ py

___ print_hanging_indents(poem):
    poem = poem.s..
    whitespace = " "
    prefix = INDENTS*whitespace
    current_line = 0
    target_poem    # list
    ___ line __ poem.splitlines
        # adjust counters
        line = line.s..
        __ line __ "":
            current_line = 0
            continue
        ____:
            current_line = current_line + 1
        # check the line we're dealing with
        __ current_line __ 0:
            new = ""
        ____ current_line __ 1:
            new = line
        ____ current_line > 1:
            new = prefix + line
        target_poem.a..(new)
    tar = '\n'.j..(target_poem)
    r.. tar

# part of William Shakespeare's play Hamlet
shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """

shakespeare_formatted = """
To be, or not to be, that is the question:
    Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
    Or to take Arms against a Sea of troubles,
"""

# part of Remember, by Christina Rosetti
rosetti_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """


rosetti_formatted = """
Remember me when I am gone away,
    Gone far away into the silent land;
    When you can no more hold me by the hand,
Nor I half turn to go yet turning stay.
Remember me when no more day by day
    You tell me of our future that you planned:
    Only remember me; you understand
"""


___ test_shakespeare_text(capfd):
    print_hanging_indents(shakespeare_unformatted)
    output = capfd.readouterr()[0]
    ... output.s.. __ shakespeare_formatted.s..


___ test_rosetti_poem(capfd):
    print_hanging_indents(rosetti_unformatted)
    output = capfd.readouterr()[0]
    ... output.s.. __ rosetti_formatted.s..


    test_rosetti_poem()
    test_shakespeare_text()