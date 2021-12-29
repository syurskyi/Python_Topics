import textwrap
import itertools

COL_WIDTH = 20


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""


    paragraphs = text.split('\n\n')
    number_of_columns = len(paragraphs)

    l = [] 
    for paragraph in paragraphs:
        paragraph = paragraph.strip()
        r = textwrap.wrap(paragraph,width=COL_WIDTH,break_long_words=True)
        l.append(r)
    
    
    

    result = []
    for p in itertools.zip_longest(*l,fillvalue=''):
        
        line = []
        for value in p:
            line.append(f"{value:<25}")

            #result.append(f"{value:<25}",end='')
            #print(f"{value:<25}",end='')
        #print()

        result.append(''.join(line))

    
    return '\n'.join(result)


if __name__ == "__main__":


    text = """My house is small but cosy.

    It has a white kitchen and an empty fridge."""
    text = """My house is small but cosy.

    It has a white kitchen and an empty fridge.

    I have a very comfortable couch, people love to sit on it."""


    text_to_columns(text)

