import re

def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    passwd = passwd.splitlines()
    passwd = [line for line in passwd if line.strip()]
    keys = []
    values = []
    for p in passwd:
        keys.append(p.split(':')[0])
        if len(p.split(':')[4]) == 0:
            values.append('unknown')
        else:
            values.append(' '.join(
                re.sub(',',' ', p.split(':')[4]).split()))
    return dict(zip(keys, values))