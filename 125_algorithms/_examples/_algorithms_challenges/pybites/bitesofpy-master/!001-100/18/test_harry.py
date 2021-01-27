from harry import get_harry_most_common_word


def test_get_harry_most_common_word():
    top_word = get_harry_most_common_word()
    a__ type(top_word) == tuple
    a__ top_word[0] == 'dursley'
    a__ top_word[1] == 45