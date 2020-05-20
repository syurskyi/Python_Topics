_____ ?


def upper_word(raw):
    r_ raw.upper()


conn _ ?.c..(':memory:')
?.create_function('upper1', 1, upper_word)
cur _ ?.c..

cur.e.. 'C.. T.. users(first_name char(20))')
cur.e..
    'I.. I.. users(first_name) V.. ("Eugene"),("Dmitry"),("Viktor")'
)
cur.e.. 'S.. upper1(first_name) F.. users')
row _ cur.fetchone()
print(row)
