#!/usr/bin/env python3


____ nlp ______ unigramtagger
____ col.. ______ Counter
______ pytest
______ pickle
______ tempfile


@pytest.fixture
___ corpus(request

    corpus _ [('train', 'VERB'), ('train', 'VERB'), ('train', 'NOUN')]

    r_ corpus

@pytest.mark.tagger
___ test_train(corpus

    ut _ unigramtagger.UnigramTagger()

    expected_model _ {
        'train': {'VERB': 2, 'NOUN': 1}
    }

    ut.train(corpus)

    a.. ut.model __ expected_model

@pytest.mark.tagger
___ test_tag_distribution(corpus

    ut _ unigramtagger.UnigramTagger()
    ut.train(corpus)

    expected_distribution _ {
        'VERB': 2/3,
        'NOUN': 1/3
    }

    a.. ut.N __ 3
    a.. ut.tag_distribution __ expected_distribution

@pytest.mark.tagger
___ test_tag(corpus

    ut _ unigramtagger.UnigramTagger()
    ut.train(corpus)

    expected_list _ [('train', 'VERB')]

    words_to_tag _ ['train']
    tagged_words _ ut.tag(words_to_tag)

    a.. expected_list __ tagged_words

@pytest.mark.filesystem
___ test_save(corpus

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

    a.. expected_data __ actual_data

@pytest.mark.filesystem
___ test_load(corpus

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

    a.. (
        expected_model __ ut.model an.
        expected_distribution __ ut.tag_distribution
    )
