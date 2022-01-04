____ s__ _______ ascii_lowercase

'''
Bite 105. Slice and dice
Take the block of text provided and strip off the whitespace at both ends. Split the text by newline (\n) using split.

Loop through the lines and if the first character of each (stripped) line is lowercase, split the line into words and 
add the last word to the (given) results list, stripping the trailing dot (.) and exclamation mark (!) from the end of 
the word.

At the end of the function return the results list.
'''


text = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""

___ my_slice_and_dice(text=text):
    """Strip the whitespace (newlines) off text at both ends,
       split the text string on newline (\n).
       Next check if the first char of each (stripped) line is lowercase,
       if so split the line into words and append the last word to
       the results list. Make sure the you strip off any trailing
       exclamation marks (!) and dots (.), Return the results list."""
    results    # list
    s = text.s...s..('\n')
    ___ item __ s:
        item = item.s..
        __ item[0].isl..
            item = item.rstrip('!')
            item = item.rstrip('.')
            words = item.s..(' ')
            results.a..(words[words.__len__()-1])
    r.. results

___ slice_and_dice(text=text):
    """Strip the whitespace (newlines) off text at both ends,
       split the text string on newline (\n).
       Next check if the first char of each (stripped) line is lowercase,
       if so split the line into words and append the last word to
       the results list. Make sure the you strip off any trailing
       exclamation marks (!) and dots (.), Return the results list."""
    results    # list
    ___ line __ text.s...s..('\n'):
        line = line.s..

        __ line[0] n.. __ ascii_lowercase:
            continue
        words = line.s.. 

        last_word_stripped = words[-1].rstrip('!.')
        results.a..(last_word_stripped)

    r.. results

slice_and_dice(text)