____ slicing _______ text, slice_and_dice

another_text = """
Take the block of text provided and strip() off the whitespace at the ends.
Split the whole block up by newline (\n).
 if the first character is lowercase, split it into words and add the last word
of that line to the results list.
Strip the trailing dot (.) and exclamation mark (!) from the word first.
  finally return the results list!
"""


___ test_slice_and_dice_default_text():
    expected = ['objects', 'y', 'too', ':)', 'bites']
    ... slice_and_dice(text) __ expected


___ test_slice_and_dice_other_text():
    expected = ['word', 'list', 'list']
    ... slice_and_dice(another_text) __ expected