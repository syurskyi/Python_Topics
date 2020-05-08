#!/usr/bin/env python3


from nlp import unigramtagger
from collections import Counter
import pytest
import pickle
import tempfile


@pytest.fixture
def corpus(request):

    corpus = [('train', 'VERB'), ('train', 'VERB'), ('train', 'NOUN')]

    return corpus

@pytest.mark.tagger
def test_train(corpus):

    ut = unigramtagger.UnigramTagger()

    expected_model = {
        'train': {'VERB': 2, 'NOUN': 1}
    }

    ut.train(corpus)

    assert ut.model == expected_model

@pytest.mark.tagger
def test_tag_distribution(corpus):

    ut = unigramtagger.UnigramTagger()
    ut.train(corpus)

    expected_distribution = {
        'VERB': 2/3,
        'NOUN': 1/3
    }

    assert ut.N == 3
    assert ut.tag_distribution == expected_distribution

@pytest.mark.tagger
def test_tag(corpus):

    ut = unigramtagger.UnigramTagger()
    ut.train(corpus)

    expected_list = [('train', 'VERB')]

    words_to_tag = ['train']
    tagged_words = ut.tag(words_to_tag)

    assert expected_list == tagged_words

@pytest.mark.filesystem
def test_save(corpus):

    testfile = tempfile.NamedTemporaryFile()

    ut = unigramtagger.UnigramTagger()
    ut.train(corpus)

    expected_data = (
        {'train': Counter(VERB=2, NOUN=1)},
        {'VERB': 2/3,
         'NOUN': 1/3
        }
    )

    ut.save(testfile.name)
    actual_data = pickle.load(testfile)

    assert expected_data == actual_data

@pytest.mark.filesystem
def test_load(corpus):

    testfile = tempfile.NamedTemporaryFile()

    ut = unigramtagger.UnigramTagger()

    # For saving a file to load later
    _ut_saver = unigramtagger.UnigramTagger()
    _ut_saver.train(corpus)
    _ut_saver.save(testfile.name)

    expected_distribution = {
        'VERB': 2/3,
        'NOUN': 1/3
    }

    expected_model = {'train': Counter(VERB=2, NOUN=1)}

    ut.load(testfile.name)

    assert (
        expected_model == ut.model and
        expected_distribution == ut.tag_distribution
    )
