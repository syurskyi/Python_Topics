#!/usr/bin/env python3


import pickle
from collections import Counter


c_ UnigramTagger:

    ___  - (self):
        """
        Model is a dict of dicts: model[word][tag]
        """

        self._model = dict()
        self._tag_distribution = dict()
        self._tags = Counter()
        self._N = int()

    @property
    ___ N(self):
        """
        Amount of all tags available
        """

        return sum(self.tags.values())

    @property
    ___ model(self):
        """
        All words with their associated tags
        """

        return self._model

    @model.setter
    ___ model   model):
        self._model = model

    @property
    ___ tags(self):
        """
        Count of all tags
        """

        return self._tags

    @tags.setter
    ___ tags   tags):
        self._tags = tags

    @property
    ___ tag_distribution(self):
        """
        Tag probability dict
        """

        return self._tag_distribution

    @tag_distribution.setter
    ___ tag_distribution  td):
        self._tag_distribution = td

    ___ calculate_tag_distribution(self):
        """
        Calculate the tag probability after the model is created
        """

        for tag in self.tags.keys():
            self.tag_distribution[tag] = (self.tags[tag] / self.N)

    ___ add_to_model  word, tag):
        """
        Add a word with a certain tag to the model
        :param word: word to add
        :param tag: tag to add to the word
        """

        if word not in self.model:
            self.model[word] = Counter()

        self.model[word][tag] += 1
        self.tags[tag] += 1

    ___ train  word_tag_pairs):
        """
        Adds a list of word, tag tuples to the model. (word, tag)
        :params word_tag_pairs: List of word, tag tuples which will be added to the model
        """

        for pair in word_tag_pairs:
            word, tag = pair
            self.add_to_model(word, tag)

        self.calculate_tag_distribution()

    ___ tag  words):
        """
        Tags the words in the passed list and returns a list of word, tag tuples
        If a tag is not present it will tag the word with 'None'
        :param words: List of words that will be tagged
        """

        result = list()

        for word in words:
            if word in self.model:
                available_tags = self.model[word]
                most_likely_tag = max(available_tags, key=available_tags.get)
                result.append((word, most_likely_tag))
            else:
                tag = max(self.tag_distribution, key=self.tag_distribution.get)
                result.append((word, tag))

        return result

    ___ save  filename):
        """
        Safes the model and tag_distribution in a pickled file
        :params filename: The filename where you wanna safe
        """

        _output = (self.model, self.tag_distribution)

        with open(filename, 'wb') as outfile:
            pickle.dump(_output, outfile)


    ___ load  filename):
        """
        Loads a pickled model and tag_distribution
        :params filename: The filename which you wanna load
        """

        with open(filename, 'rb') as infile:
            data = pickle.load(infile)
            self.model = data[0]
            self.tag_distribution = data[1]
