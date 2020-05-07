#!/usr/bin/env python3


from nlp import unigramtagger
from collections import Counter
import unittest
import pickle
import tempfile


class UtilTest(unittest.TestCase):
    """
    Class for the test function
    """

    def corpus(self):

        corpus = [('train', 'VERB'), ('train', 'VERB'), ('train', 'NOUN')]

        return corpus


    def test_train(self):

        corpus = self.corpus()
        ut = unigramtagger.UnigramTagger()

        expected_model = {
            'train': {'VERB': 2, 'NOUN': 1}
        }


        ut.train(corpus)

        self.assertEqual(ut.model, expected_model)


    def test_tag_distribution(self):

        corpus = self.corpus()
        ut = unigramtagger.UnigramTagger()

        ut.train(corpus)

        expected_distribution = {
            'VERB': 2/3,
            'NOUN': 1/3
        }

        self.assertEqual(ut.N, 3)
        self.assertEqual(ut.tag_distribution, expected_distribution)


    def test_tag(self):

        corpus = self.corpus()
        ut = unigramtagger.UnigramTagger()

        ut.train(corpus)

        expected_list = [('train', 'VERB')]

        words_to_tag = ['train']
        tagged_words = ut.tag(words_to_tag)

        self.assertEqual(expected_list, tagged_words)


    def test_save(self):

        corpus = self.corpus()
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

        self.assertEqual(expected_data, actual_data)


    def test_load(self):

        corpus = self.corpus()
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

        self.assertEqual(expected_model,ut.model)
        self.assertEqual(expected_distribution, ut.tag_distribution)


if __name__ == '__main__':
        unittest.main()
