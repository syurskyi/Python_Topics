from test_sentences import *
import re

___ capitalize_sentences(text: str) -> str:
   """Return text capitalizing the sentences. Note that sentences can end
      in dot (.), question mark (?) and exclamation mark (!)"""

   text_metacharacters = re.findall("[\\!\\.\\?]", text.strip())
   text_raw = re.split("[\\!\\.\\?]\s", text.strip())

   text_clean = []
   for i in range(len(text_raw)):
      text_clean.append(f"{text_raw[i].capitalize()}{(text_metacharacters[i] __ i != len(text_metacharacters) -1 else '')}")
   return " ".join(text_clean)


__ __name__ == "__main__":
   print(capitalize_sentences(" ".join(text2).lower()))