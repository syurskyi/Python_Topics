_______ p__

____ chaining_docs _______ Document


EOL_PUNCTUATION = ".!?"

DOCS = {
    "four-liner": (
        Document()
        .add_line("first")
        .add_line("fourth")
        .add_line("third", 1)
        .add_line("second", 1)
    ),
    "tale": (
        Document()
        .add_line("This is the tale of a dwarf.")
        .add_line("")
        .add_line("A dwarf you ask?")
        .add_line("Yes, a dwarf and not any dwarf, so you know!")
    ),
    "complex": (
        Document()
        .add_line("My second sentence.")
        .add_line("My first sentence.")
        .swap_lines(0, 1)
        .add_line("Introduction", 0)
        .add_punctuation("!", 0)
        .add_line("")
        .add_line("My second paragraph.")
        .merge_lines([1, 2])
    ),
    "edgy": (
        Document().add_line("").swap_lines(0, 0).merge_lines([0]).add_punctuation(".", 0)
    ),
    "full-case": (
        Document()
        .add_line("1")  # 1
        .add_line("2", 0)  # 2\n1
        .add_line("3", 1)  # 2\n3\n1
        .swap_lines(0, 1)  # 3\n2\n1
        .swap_lines(1, 2)  # 3\n1\n2
        .swap_lines(2, 1)  # 3\n2\n1
        .merge_lines([0, 2])  # 3 1\n2
        .merge_lines([0, 1])  # 3 1 2
    ),
    "punctuation": (
        Document()
        .add_line("")
        .add_punctuation(".", 0)
        .add_punctuation("!", 0)
        .add_punctuation("?", 0)
        .add_line(".")
        .add_punctuation("?", 1)  # ?\n?
    ),
}


@p__.f..()
___ doc(request):
    """Factory method for test documents"""
    r.. DOCS.get(request.param, Document())


@p__.m__.p..(
    "doc, expected",
    [
        ("complex", Document),
    ],
    indirect=["doc"],
)
___ test_correct_return_type(doc, expected):
    ... isi..(doc, expected)


@p__.m__.p..(
    "doc, expected",
    [
        ("tale", 4),
        ("complex", 4),
        ("four-liner", 4),
        ("edgy", 1),
        ("full-case", 1),
        ("punctuation", 2),
    ],
    indirect=["doc"],
)
___ test_len_implementation(doc, expected):
    ... l..(doc) __ expected


@p__.m__.p..(
    "doc, expected",
    [
        ("tale", 21),
        ("complex", 10),
        ("four-liner", 4),
        ("edgy", 0),
        ("full-case", 3),
        ("punctuation", 0),
    ],
    indirect=["doc"],
)
___ test_word_count_implementation(doc, expected):
    ... doc.word_count() __ expected


@p__.m__.p..(
    "doc, expected",
    [
        ("four-liner", "first\nsecond\nthird\nfourth"),
        (
            "tale",
            "This is the tale of a dwarf.\n\nA dwarf you ask?\nYes, a dwarf and not any dwarf, so you know!",
        ),
        (
            "complex",
            "Introduction!\nMy first sentence. My second sentence.\n\nMy second paragraph.",
        ),
        ("edgy", "."),
        ("full-case", "3 1 2"),
        ("punctuation", "?\n?"),
    ],
    indirect=["doc"],
)
___ test_correct_chaining(doc, expected):
    ... s..(doc) __ expected


@p__.m__.p..(
    "doc, expected",
    [
        (
            "tale",
            s..(
                [
                    "this",
                    "is",
                    "the",
                    "tale",
                    "of",
                    "a",
                    "dwarf",
                    "you",
                    "ask",
                    "yes",
                    "and",
                    "not",
                    "any",
                    "so",
                    "know",
                ]
            ),
        ),
        (
            "complex",
            s..(["my", "first", "second", "sentence", "introduction", "paragraph"]),
        ),
        ("edgy", []),
        ("full-case", ["1", "2", "3"]),
        ("punctuation", []),
    ],
    indirect=["doc"],
)
___ test_words_property(doc, expected):
    ... doc.words __ expected