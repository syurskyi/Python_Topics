____ unittest ______ TestCase
____ my_package ______ MyApp

c_ TestOperations(TestCase):
    ___ setUp
        app _ MyApp()
    ___ test_add
        assertEqual(app.do('add', 3, 4), 7)
        assertEqual(app.do('ADD', 3, 4), 7)
    ___ test_multiply
        assertEqual(app.do('multiply', 3, 4), 12)
    ___ test_substract
        assertEqual(app.do('substract', 3, 4), -1)
