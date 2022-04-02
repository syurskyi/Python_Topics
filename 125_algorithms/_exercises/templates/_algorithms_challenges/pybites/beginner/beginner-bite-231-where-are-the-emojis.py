"""
In this Bite you are given a list of strings that contain emojis.
Complete get_emoji_indices returning a list of indices of the emojis found in the text.

Here is an example how it should work:

>>> from emojis import get_emoji_indices
>>> text = "We see more and more 🐍 Python 🥋 ninjas, keep it up 💪"
>>> text.index('🐍')
21
>>> text.index('🥋')
30
>>> text.index('💪')
51
>>> get_emoji_indices(text)
[21, 30, 51]
"""

_______ __
____ typing _______ List

# https://stackoverflow.com/a/43147265
# just for exercise sake, real life use emoji lib
IS_EMOJI  __.c..(r'[^\w\s,]')


___ get_emoji_indices(text: s..) __ List[i..]:
    """Given a text return indices of emoji characters"""
    p..