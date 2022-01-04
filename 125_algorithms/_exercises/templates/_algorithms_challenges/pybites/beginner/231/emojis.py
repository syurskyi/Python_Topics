_______ __
____ typing _______ List

# https://stackoverflow.com/a/43147265
# just for exercise sake, real life use emoji lib
IS_EMOJI = __.c..(r'[^\w\s,]')


___ get_emoji_indices(text: s..) -> List[int]:
    """Given a text return indices of emoji characters"""
    r.. [i ___ i __ r..(l..(text)) __ IS_EMOJI.m..(text,i)]
    #for i in range(len(text)):
    #    if IS_EMOJI.match(text, i):
    #        print(i)
    #    #print(IS_EMOJI.search(char))

print(get_emoji_indices('We 💜 Python 🐍'))