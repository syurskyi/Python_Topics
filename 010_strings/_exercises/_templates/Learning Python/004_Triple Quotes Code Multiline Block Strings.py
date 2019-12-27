mantra = """Always look
on the bright
side of life."""

print(mantra)


menu = """spam # comments here added to string!
... eggs # ditto
... """
print(menu)
'spam # comments here added to string!\neggs # ditto\n'
menu = (
"...spam\n"  # comments here ignored
"...eggs\n"  # but newlines not automatic
)
print(menu)


