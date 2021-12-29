INDENTS = 4

shakespeare_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """

def print_hanging_indents(poem):
    poem_line = [line.strip() for line in poem.split('\n')]
    """ if poem_line[0] == "":
        poem_line = poem_line[1:]
    if poem_line[-1] == "":
        poem_line = poem_line[:-1] """
    previous_line = ""
    for line in poem_line:
        if len(line) != 0:
            if previous_line == "":
                print(line)
            else:
                print(f"    "+line)
        previous_line = line


#print_hanging_indents(shakespeare_unformatted)