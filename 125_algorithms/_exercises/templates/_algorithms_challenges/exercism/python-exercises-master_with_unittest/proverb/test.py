_______ unittest

____ proverb _______ proverb


c_ ProverbTest(unittest.TestCase):
    ___ test_a_single_consequence
        expected = 'For want of a nail the shoe was lost.\n'\
                   'And all for the want of a nail.'
        assertEqual(proverb(['nail', 'shoe']), expected)

    ___ test_short_list
        expected = 'For want of a nail the shoe was lost.\n'\
                   'For want of a shoe the horse was lost.\n'\
                   'And all for the want of a nail.'
        assertEqual(proverb(['nail', 'shoe', 'horse']), expected)

    ___ test_long_list
        expected = 'For want of a nail the shoe was lost.\n'\
                   'For want of a shoe the horse was lost.\n'\
                   'For want of a horse the rider was lost.\n'\
                   'And all for the want of a nail.'
        assertEqual(proverb(['nail', 'shoe', 'horse', 'rider']), expected)

    ___ test_new_itens
        expected = 'For want of a key the value was lost.\n'\
                   'And all for the want of a key.'
        assertEqual(proverb(['key', 'value']), expected)

    ___ test_whole_proverb
        expected = 'For want of a nail the shoe was lost.\n'\
                   'For want of a shoe the horse was lost.\n'\
                   'For want of a horse the rider was lost.\n'\
                   'For want of a rider the message was lost.\n'\
                   'For want of a message the battle was lost.\n'\
                   'For want of a battle the kingdom was lost.\n'\
                   'And all for the want of a nail.'
        assertEqual(
            proverb([
                'nail', 'shoe', 'horse', 'rider', 'message', 'battle',
                'kingdom'
            ]), expected)

    ___ test_qualifier
        expected = 'For want of a nail the shoe was lost.\n'\
                   'For want of a shoe the horse was lost.\n'\
                   'For want of a horse the rider was lost.\n'\
                   'For want of a rider the message was lost.\n'\
                   'For want of a message the battle was lost.\n'\
                   'For want of a battle the kingdom was lost.\n'\
                   'And all for the want of a horseshoe nail.'
        assertEqual(
            proverb(
                [
                    'nail', 'shoe', 'horse', 'rider', 'message', 'battle',
                    'kingdom'
                ],
                qualifier='horseshoe'), expected)


__ __name__ __ '__main__':
    unittest.main()
