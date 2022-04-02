_______ unicodedata

___ filter_accents(text
   """Return a sequence of accented characters found in
      the passed in lowercased text string
   """
   accent_chars    # list
   ___ i __ r..(l..(text)):
      char = unicodedata.normalize("NFD", text[i]).encode("ascii", "ignore").d.. "utf-8")

      __ char.l.. __ text[i].l..:
         _____
      ____:
         accent_chars.a..(text[i].l..

   r.. accent_chars


# if __name__ == "__main__":
#    print(filter_accents("The cédille (cedilla) Ç ..."))