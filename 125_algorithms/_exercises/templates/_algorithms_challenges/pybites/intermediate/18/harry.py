_______ os
_______ urllib.request
_______ __
____ collections _______ Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.j..(tmp, 'stopwords')
harry_text = os.path.j..(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


___ get_harry_most_common_word

    # Stopwords
    with open(stopwords_file) __ file:
        stopwords = [word.s.. ___ word __ file]

    # Harry text
    with open(harry_text) __ file:
        content_remove_apos = [line.r..("'", "").r..("’", "") ___ line __ file]
        harry_content = [__.sub(r"\W+", " ", line).s...l.. ___ line __ content_remove_apos]

        final_words    # list
        ___ line __ harry_content:
            current_line = line.s..(" ")
            ___ word __ current_line:
                __ word __ "":
                    continue
                __ word n.. __ stopwords:
                    final_words.a..(word)

        counter = Counter(final_words)
        r.. counter.most_common()[0]