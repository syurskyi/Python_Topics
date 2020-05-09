#!/usr/bin/env python3


____ nlp ______ unigramtagger
____ collections ______ Counter
______ unittest
______ pickle
______ tempfile


c_ UtilTest(unittest.TestCase):
    """
    Class for the test function
    """

    ___ corpus

        corpus _ [('train', 'VERB'), ('train', 'VERB'), ('train', 'NOUN')]

        r_ corpus


    ___ test_train

        corpus _ corpus()
        ut _ unigramtagger.UnigramTagger()

        expected_model _ {
            'train': {'VERB': 2, 'NOUN': 1}
        }


        ut.train(corpus)

        assertEqual(ut.model, expected_model)


    ___ test_tag_distribution

        corpus _ corpus()
        ut _ unigramtagger.UnigramTagger()

        ut.train(corpus)

        expected_distribution _ {
            'VERB': 2/3,
            'NOUN': 1/3
        }

        assertEqual(ut.N, 3)
        assertEqual(ut.tag_distribution, expected_distribution)


    ___ test_tag

        corpus _ corpus()
        ut _ unigramtagger.UnigramTagger()

        ut.train(corpus)

        expected_list _ [('train', 'VERB')]

        words_to_tag _ ['train']
        tagged_words _ ut.tag(words_to_tag)

        assertEqual(expected_list, tagged_words)


    ___ test_save

        corpus _ corpus()
        testfile _ tempfile.NamedTemporaryFile()

        ut _ unigramtagger.UnigramTagger()
        ut.train(corpus)

        expected_data _ (
            {'train': Counter(VERB_2, NOUN_1)},
            {'VERB': 2/3,
             'NOUN': 1/3
            }
        )

        ut.save(testfile.name)
        actual_data _ pickle.load(testfile)

        assertEqual(expected_data, actual_data)


    ___ test_load

        corpus _ corpus()
        testfile _ tempfile.NamedTemporaryFile()

        ut _ unigramtagger.UnigramTagger()

        # For saving a file to load later
        _ut_saver _ unigramtagger.UnigramTagger()
        _ut_saver.train(corpus)
        _ut_saver.save(testfile.name)

        expected_distribution _ {
            'VERB': 2/3,
            'NOUN': 1/3
        }

        expected_model _ {'train': Counter(VERB_2, NOUN_1)}

        ut.load(testfile.name)

        assertEqual(expected_model,ut.model)
        assertEqual(expected_distribution, ut.tag_distribution)


if __name__ == '__main__':
        unittest.main()
