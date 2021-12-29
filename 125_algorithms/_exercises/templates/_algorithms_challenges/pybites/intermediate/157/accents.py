import unicodedata

___ filter_accents(text):
   """Return a sequence of accented characters found in
      the passed in lowercased text string
   """
   accent_chars = []
   for i in range(len(text)):
      char = unicodedata.normalize("NFD", text[i]).encode("ascii", "ignore").decode("utf-8")

      __ char.lower() == text[i].lower():
         continue
      else:
         accent_chars.append(text[i].lower())

   return accent_chars


# if __name__ == "__main__":
#    print(filter_accents("The cédille (cedilla) Ç ..."))