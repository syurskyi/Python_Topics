#!python3
#reverse_list.py is a quick script to reverse the order of a list copied to the clipboard

______ pyperclip

___ paste_from_clipboard(
	text = pyperclip.paste().split("\r")
	r_ text
	
___ copy_to_clipboard(new_list
	new_list[-1] = '\n' + new_list[-1]
	new_text = ''.join(new_list)
	pyperclip.copy(new_text)
	print("The new string is now copied to the clipboard. Hit CTRL V to paste.")
	
___ reverse_list(text_list
	text_list.reverse()
	r_ text_list

__ __name__ __ "__main__":
	new_list = reverse_list(paste_from_clipboard())
	copy_to_clipboard(new_list)
