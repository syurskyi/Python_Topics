# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to find the occurrence and position of the substrings within a string.
# 
# Input
# text = 'Python exercises, PHP exercises, C# exercises'
# pattern = 'exercises'
# 
# Output
# Found "exercises" at 7:16                                                                                     
# Found "exercises" at 22:31                                                                                    
# Found "exercises" at 36:45

import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))
	


