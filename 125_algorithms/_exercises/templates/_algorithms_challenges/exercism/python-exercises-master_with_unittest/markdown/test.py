_______ unittest
____ markdown _______ parse_markdown


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

c_ MarkdownTest(unittest.TestCase):

    ___ test_paragraph
        assertEqual(parse_markdown('This will be a paragraph'),
                         '<p>This will be a paragraph</p>')

    ___ test_italics
        assertEqual(parse_markdown('_This will be italic_'),
                         '<p><em>This will be italic</em></p>')

    ___ test_bold
        assertEqual(parse_markdown('__This will be bold__'),
                         '<p><strong>This will be bold</strong></p>')

    ___ test_mixed_normal_italics_and_bold
        assertEqual(parse_markdown('This will _be_ __mixed__'),
                         '<p>This will <em>be</em> <strong>mixed</strong></p>')

    ___ test_h1
        assertEqual(parse_markdown('# This will be an h1'),
                         '<h1>This will be an h1</h1>')

    ___ test_h2
        assertEqual(parse_markdown('## This will be an h2'),
                         '<h2>This will be an h2</h2>')

    ___ test_h6
        assertEqual(parse_markdown(
            '###### This will be an h6'), '<h6>This will be an h6</h6>')

    ___ test_unordered_lists
        assertEqual(parse_markdown('* Item 1\n* Item 2'),
                         '<ul><li>Item 1</li>'
                         '<li>Item 2</li></ul>')

    ___ test_little_bit_of_everything
        assertEqual(parse_markdown(
            '# Header!\n* __Bold Item__\n* _Italic Item_'),
            '<h1>Header!</h1><ul><li><strong>Bold Item</strong></li>'
            '<li><em>Italic Item</em></li></ul>')


__ _____ __ _____
    unittest.main()
