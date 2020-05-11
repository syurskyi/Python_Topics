#!/usr/bin/env python3


____ nlp ______ unigramtagger
____ col.. ______ Counter
______ u__
______ pickle
______ tempfile


c_ UtilTest?.?
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

        aE..(ut.model, expected_model)


    ___ test_tag_distribution

        corpus _ corpus()
        ut _ unigramtagger.UnigramTagger()

        ut.train(corpus)

        expected_distribution _ {
            'VERB': 2/3,
            'NOUN': 1/3
        }

        aE..(ut.N, 3)
        aE..(ut.tag_distribution, expected_distribution)


    ___ test_tag

        corpus _ corpus()
        ut _ unigramtagger.UnigramTagger()

        ut.train(corpus)

        expected_list _ [('train', 'VERB')]

        words_to_tag _ ['train']
        tagged_words _ ut.tag(words_to_tag)

        aE..(expected_list, tagged_words)


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
        actual_data _ pickle.l..(testfile)

        aE..(expected_data, actual_data)


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

        ut.l..(testfile.name)

        aE..(expected_model,ut.model)
        aE..(expected_distribution, ut.tag_distribution)


__ _____ __ _____
        ?.?
