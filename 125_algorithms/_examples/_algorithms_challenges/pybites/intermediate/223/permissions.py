def get_octal_from_file_permission(rwx: str) -> str:
   """Receive a Unix file permission and convert it to
      its octal representation.

      In Unix you have user, group and other permissions,
      each can have read (r), write (w), and execute (x)
      permissions expressed by r, w and x.

      Each has a number:
      r = 4
      w = 2
      x = 1

      So this leads to the following input/ outputs examples:
      rw-r--r-- => 644 (user = 4 + 2, group = 4, other = 4)
      rwxrwxrwx => 777 (user/group/other all have 4 + 2 + 1)
      r-xr-xr-- => 554 (user/group = 4 + 1, other = 4)
   """
   octal_lookup = {
      "r": 4,
      "w": 2,
      "x": 1
   }

   octal_c = [octal_lookup[char] if char in octal_lookup else 0 for char in rwx]
   octal_file = [str(sum(octal_c[i:j])) for i, j in zip(range(0, len(octal_c), 3), range(3, len(octal_c) +1, 3))]
   return "".join(octal_file)


# if __name__ == "__main__":
#    print(get_octal_from_file_permission('-----x-w-'))