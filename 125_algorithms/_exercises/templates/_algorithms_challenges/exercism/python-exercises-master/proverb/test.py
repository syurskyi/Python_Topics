______ unittest

from proverb ______ proverb


class ProverbTest(unittest.TestCase
    ___ test_a_single_consequence(self
        expected = 'For want of a nail the shoe was lost.\n'\
                   'And all for the want of a nail.'
        self.assertEqual(proverb(['nail', 'shoe']), expected)

    ___ test_short_list(self
        expected = 'For want of a nail the shoe was lost.\n'\
                   'For want of a shoe the horse was lost.\n'\
                   'And all for the want of a nail.'
        self.assertEqual(proverb(['nail', 'shoe', 'horse']), expected)

    ___ test_long_list(self
        expected = 'For want of a nail the shoe was lost.\n'\
                   'For want of a shoe the horse was lost.\n'\
                   'For want of a horse the rider was lost.\n'\
                   'And all for the want of a nail.'
        self.assertEqual(proverb(['nail', 'shoe', 'horse', 'rider']), expected)

    ___ test_new_itens(self
        expected = 'For want of a key the value was lost.\n'\
                   'And all for the want of a key.'
        self.assertEqual(proverb(['key', 'value']), expected)

    ___ test_whole_proverb(self
        expected = 'For want of a nail the shoe was lost.\n'\
                   'For want of a shoe the horse was lost.\n'\
                   'For want of a horse the rider was lost.\n'\
                   'For want of a rider the message was lost.\n'\
                   'For want of a message the battle was lost.\n'\
                   'For want of a battle the kingdom was lost.\n'\
                   'And all for the want of a nail.'
        self.assertEqual(
            proverb([
                'nail', 'shoe', 'horse', 'rider', 'message', 'battle',
                'kingdom'
            ]), expected)

    ___ test_qualifier(self
        expected = 'For want of a nail the shoe was lost.\n'\
                   'For want of a shoe the horse was lost.\n'\
                   'For want of a horse the rider was lost.\n'\
                   'For want of a rider the message was lost.\n'\
                   'For want of a message the battle was lost.\n'\
                   'For want of a battle the kingdom was lost.\n'\
                   'And all for the want of a horseshoe nail.'
        self.assertEqual(
            proverb(
                [
                    'nail', 'shoe', 'horse', 'rider', 'message', 'battle',
                    'kingdom'
                ],
                qualifier='horseshoe'), expected)


__ __name__ __ '__main__':
    unittest.main()
