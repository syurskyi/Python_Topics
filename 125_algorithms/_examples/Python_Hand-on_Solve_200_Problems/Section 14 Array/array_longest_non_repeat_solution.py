# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Challenge
# Given a string, find the length of the longest substring
# without repeating characters.

# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3.
# ---------------------------------------------------------------
# Algorithm

# In summary : Form all posible sub_strings from original string, then return length of longest sub_string

# - start from 1st character, form as long as posible sub string

#             - Add first character to sub string
#             - Add second character to sub string if second character not exist in sub string
#             ...
#             - Repeate until got a character which already exist inside sub string or 
    
    
# - start from 2nd character, form as long as posible sub string

#             - Add first character to sub string
#             - Add second character to sub string if second character not exist in sub string
#             ...
#             - Repeate until got a character which already exist inside sub string


# ....


# - start from final character, form as long as posible sub string
#             - Add first character to sub string
#             - Add second character to sub string if second character not exist in sub string
#             ...
#             - Repeate until got a character which already exist inside sub string
# ---------------------------------------------------------------

str = "abcbb"

def longest_non_repeat(str):
    
    # init start position and max length     
    i=0
    max_length = 1

    for i,c in enumerate(str):

        # init counter and sub string value         
        start_at = i
        sub_str=[]

        # continue increase sub string if did not repeat character         
        while (start_at < len(str)) and (str[start_at] not in sub_str):
            sub_str.append(str[start_at])
            start_at = start_at + 1

        # update the max length   
        if len(sub_str) > max_length:
            max_length = len(sub_str)

        print(sub_str)
        
    return max_length

longest_non_repeat(str)


