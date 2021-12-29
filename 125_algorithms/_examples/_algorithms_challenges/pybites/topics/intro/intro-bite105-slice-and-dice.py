from string import ascii_lowercase

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

def my_slice_and_dice(text=text):
    """Strip the whitespace (newlines) off text at both ends,
       split the text string on newline (\n).
       Next check if the first char of each (stripped) line is lowercase,
       if so split the line into words and append the last word to
       the results list. Make sure the you strip off any trailing
       exclamation marks (!) and dots (.), Return the results list."""
    results = []
    s = text.strip().split('\n')
    for item in s:
        item = item.strip()
        if item[0].islower():
            item = item.rstrip('!')
            item = item.rstrip('.')
            words = item.split(' ')
            results.append(words[words.__len__()-1])
    return results

def slice_and_dice(text=text):
    """Strip the whitespace (newlines) off text at both ends,
       split the text string on newline (\n).
       Next check if the first char of each (stripped) line is lowercase,
       if so split the line into words and append the last word to
       the results list. Make sure the you strip off any trailing
       exclamation marks (!) and dots (.), Return the results list."""
    results = []
    for line in text.strip().split('\n'):
        line = line.strip()

        if line[0] not in ascii_lowercase:
            continue
        words = line.split()

        last_word_stripped = words[-1].rstrip('!.')
        results.append(last_word_stripped)

    return results

slice_and_dice(text)