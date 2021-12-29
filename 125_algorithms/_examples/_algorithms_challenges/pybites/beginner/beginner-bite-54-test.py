import pytest
import pluggy
import py

def print_hanging_indents(poem):
    poem = poem.strip()
    whitespace = " "
    prefix = INDENTS*whitespace
    current_line = 0
    target_poem = []
    for line in poem.splitlines():
        # adjust counters
        line = line.strip()
        if line == "":
            current_line = 0
            continue
        else:
            current_line = current_line + 1
        # check the line we're dealing with
        if current_line == 0:
            new = ""
        elif current_line == 1:
            new = line
        elif current_line > 1:
            new = prefix + line
        target_poem.append(new)
    tar = '\n'.join(target_poem)
    return tar

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


def test_shakespeare_text(capfd):
    print_hanging_indents(shakespeare_unformatted)
    output = capfd.readouterr()[0]
    assert output.strip() == shakespeare_formatted.strip()


def test_rosetti_poem(capfd):
    print_hanging_indents(rosetti_unformatted)
    output = capfd.readouterr()[0]
    assert output.strip() == rosetti_formatted.strip()


    test_rosetti_poem()
    test_shakespeare_text()