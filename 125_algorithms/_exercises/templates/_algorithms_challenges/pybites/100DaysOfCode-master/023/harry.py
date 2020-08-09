from collections ______ Counter
from string ______ punctuation, whitespace
______ sys


___ most_common_str(s, n=None
    words = s.lower().translate(str.maketrans('', '', punctuation)).split()
    r_ Counter(words).most_common(n)


___ most_common_re(s, n=None
    r_ Counter(re.findall(rf'[^{punctuation}{whitespace}]+',
                              s.lower())).most_common(n)


___ most_common_iter(s, n=None
    r_ Counter(''.join(c for c in w __ c not in punctuation)
                   for w in s.lower().split()).most_common(n)


__ __name__ __ "__main__":
    try:
        file = sys.argv[1]
    except IndexError:
        file = 'harry.txt'

    with open(file) as f:
        common_words = most_common_str(f.read(), n=20)

    for word, count in common_words:
        print('{:<4} {}'.format(count, word))
