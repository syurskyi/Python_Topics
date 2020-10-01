# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# 'The quick brown fox jumps over the lazy dog.'
# input : "The quick brown fox jumps over the lazy dog."
# output : "dog. lazy the over jumps fox brown quick The "

___ reverse_string_words(text):
    ___ line __ text.sp..('\n'):
        r_(' '.j..(line.sp..()[::-1]))
    
print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
print(reverse_string_words("Python Exercises."))


