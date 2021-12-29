____ test_sentences _______ *
_______ re

___ capitalize_sentences(text: str) -> str:
   """Return text capitalizing the sentences. Note that sentences can end
      in dot (.), question mark (?) and exclamation mark (!)"""

   text_metacharacters = re.findall("[\\!\\.\\?]", text.strip())
   text_raw = re.split("[\\!\\.\\?]\s", text.strip())

   text_clean    # list
   ___ i __ r..(l..(text_raw)):
      text_clean.a..(f"{text_raw[i].capitalize()}{(text_metacharacters[i] __ i != l..(text_metacharacters) -1 ____ '')}")
   r.. " ".join(text_clean)


__ __name__ __ "__main__":
   print(capitalize_sentences(" ".join(text2).lower()))