____ string _______ ascii_lowercase

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


___ slice_and_dice(text: str = text) -> l..:
    """Get a list of words from the passed in text.
       See the Bite description for step by step instructions"""
    strip = text.strip(" . !")
    split = text.split("\n")
    ___ words __ text:
        strip, split
    ___ firstword __ text:
        __ firstword.islower():
            firstword.split
    results = [""].strip.split
    r.. results