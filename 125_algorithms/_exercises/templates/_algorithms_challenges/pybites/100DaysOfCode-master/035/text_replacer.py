#!python3
#text_replacer.py replaces any text copied to the clipboard with a specified alternative.

______ pyperclip

___ paste_from_clipboard(
	text = pyperclip.paste()
	r_ text

	
___ copy_to_clipboard(new_text
	pyperclip.copy(new_text)
	print("The new string is now copied to the clipboard. Hit CTRL V to paste.")
	

___ replace_text(old_text
	target = input('What would you like to replace? ')
	replacement = input('And what would you like to replace it with? ')
	new_text = old_text.replace(target, replacement)
	r_ new_text

__  -n __ "__main__":
	old_text = paste_from_clipboard()
	new_text = replace_text(old_text)
	copy_to_clipboard(new_text)
	input()