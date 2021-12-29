import re
import pdb
def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    
    passwords = {}
    #pdb.set_trace()
    for line in passwd.splitlines():
        if not line:
            continue
        values = line.split(':')
        username,name = values[0],values[4]
        name = name.strip(',')
        if name != '':
            name = re.sub(r'\,+',' ',name)
        else:
            name = 'unknown'



        passwords[username] = name

    return passwords


if __name__ == "__main__":
    
    pw = """
postfix:x:108:112::/var/sppol/postfix
artagnon:x:1005:1005:Ramkumar R,,,,Git GSOC:/home/bin
"""

    print(get_users(pw))


