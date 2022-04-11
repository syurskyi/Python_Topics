_______ unittest

____ proverb _______ proverb


c_ ProverbTest(unittest.TestCase
    ___ test_a_single_consequence
        e.. 'For want of a nail the shoe was lost.\n'\
                   'And all for the want of a nail.'
        assertEqual(proverb( 'nail', 'shoe' ), e..)

    ___ test_short_list
        e.. 'For want of a nail the shoe was lost.\n'\
                   'For want of a shoe the horse was lost.\n'\
                   'And all for the want of a nail.'
        assertEqual(proverb( 'nail', 'shoe', 'horse' ), e..)

    ___ test_long_list
        e.. 'For want of a nail the shoe was lost.\n'\
                   'For want of a shoe the horse was lost.\n'\
                   'For want of a horse the rider was lost.\n'\
                   'And all for the want of a nail.'
        assertEqual(proverb( 'nail', 'shoe', 'horse', 'rider' ), e..)

    ___ test_new_itens
        e.. 'For want of a key the value was lost.\n'\
                   'And all for the want of a key.'
        assertEqual(proverb( 'key', 'value' ), e..)

    ___ test_whole_proverb
        e.. 'For want of a nail the shoe was lost.\n'\
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
            ]), e..)

    ___ test_qualifier
        e.. 'For want of a nail the shoe was lost.\n'\
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
                qualifier='horseshoe'), e..)


__ _____ __ _____
    unittest.main()
