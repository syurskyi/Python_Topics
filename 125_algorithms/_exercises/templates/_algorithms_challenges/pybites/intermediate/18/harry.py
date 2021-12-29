_______ os
_______ urllib.request
_______ re
____ collections _______ Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


___ get_harry_most_common_word():

    # Stopwords
    with open(stopwords_file) as file:
        stopwords = [word.strip() ___ word __ file]

    # Harry text
    with open(harry_text) as file:
        content_remove_apos = [line.replace("'", "").replace("’", "") ___ line __ file]
        harry_content = [re.sub(r"\W+", " ", line).strip().lower() ___ line __ content_remove_apos]

        final_words    # list
        ___ line __ harry_content:
            current_line = line.split(" ")
            ___ word __ current_line:
                __ word __ "":
                    continue
                __ word n.. __ stopwords:
                    final_words.a..(word)

        counter = Counter(final_words)
        r.. counter.most_common()[0]