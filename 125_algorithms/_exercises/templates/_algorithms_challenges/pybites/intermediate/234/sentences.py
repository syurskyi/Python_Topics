____ test_sentences _______ *
_______ __

___ capitalize_sentences(text: s..) __ s..:
   """Return text capitalizing the sentences. Note that sentences can end
      in dot (.), question mark (?) and exclamation mark (!)"""

   text_metacharacters __.f..("[\\!\\.\\?]", text.s..
   text_raw __.s..("[\\!\\.\\?]\s", text.s..

   text_clean    # list
   ___ i __ r..(l..(text_raw:
      text_clean.a..(f"{text_raw[i].capitalize()}{(text_metacharacters[i] __ i != l..(text_metacharacters) -1 ____ '')}")
   r.. " ".j..(text_clean)


__ _______ __ _______
   print(capitalize_sentences(" ".j..(text2).lower()))