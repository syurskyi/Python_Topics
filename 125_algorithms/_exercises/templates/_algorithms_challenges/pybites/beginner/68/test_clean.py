_______ p__

____ clean _______ remove_punctuation


@p__.mark.parametrize("input_argument, expected_return", [
    ('Hello, I am Tim.', 'Hello I am Tim'),
    (';String. with. punctuation characters!',
     'String with punctuation characters'),
    ('Watch out!!!', 'Watch out'),
    ('Spaces - should - work the same, yes?',
     'Spaces  should  work the same yes'),
    ("Some other (chars) |:-^, let's delete them",
     'Some other chars  lets delete them'),
])
___ test_remove_punctuation(input_argument, expected_return):
    ... remove_punctuation(input_argument) __ expected_return