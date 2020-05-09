#!/usr/bin/env python3


____ nlp ______ unigramtagger
____ collections ______ Counter
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

    assert ut.model == expected_model

@pytest.mark.tagger
___ test_tag_distribution(corpus

    ut _ unigramtagger.UnigramTagger()
    ut.train(corpus)

    expected_distribution _ {
        'VERB': 2/3,
        'NOUN': 1/3
    }

    assert ut.N == 3
    assert ut.tag_distribution == expected_distribution

@pytest.mark.tagger
___ test_tag(corpus

    ut _ unigramtagger.UnigramTagger()
    ut.train(corpus)

    expected_list _ [('train', 'VERB')]

    words_to_tag _ ['train']
    tagged_words _ ut.tag(words_to_tag)

    assert expected_list == tagged_words

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

    assert expected_data == actual_data

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

    assert (
        expected_model == ut.model and
        expected_distribution == ut.tag_distribution
    )
