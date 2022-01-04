____ __future__ _______ annotations
_______ string
_______ __

EOL_PUNCTUATION = ".!?"


c_ Document:
    ___ - ) __ N..
        # it is up to you how to implement this method
        # feel free to alter this method and its parameters to your liking
        lines    # list

    ___ add_line(self, line: s.., index: i.. = N..) __ Document:
        """Add a new line to the document.

        Args:
            line (str): The line,
                expected to end with some kind of punctuation.
            index (int, optional): The place where to add the line into the document.
                If None, the line is added at the end. Defaults to None.

        Returns:
            Document: The changed document with the new line.
        """
        __ index __ N..
            lines.a..(line)
        ____:
            lines.insert(index,line)
        r.. self




    ___ swap_lines(self, index_one: i.., index_two: i..) __ Document:
        """Swap two lines.

        Args:
            index_one (int): The first line.
            index_two (int): The second line.

        Returns:
            Document: The changed document with the swapped lines.
        """

        __ index_one __ index_two:
            r.. self

        try:
            lines[index_one],lines[index_two] = lines[index_two],lines[index_one]
        except IndexError:
            raise IndexError("Invalid indexes")

        r.. self

    ___ merge_lines(self, indices: l..) __ Document:

        """Merge several lines into a single line.

        If indices are not in a row, the merged line is added at the first index.

        Args:
            indices (list): The lines to be merged.

        Returns:
            Document: The changed document with the merged lines.
        """

        __ l..(indices) <= 1:
            r.. self
        
        lines    # list
        ___ index __ indices:
            lines.a..(lines[index].strip())
        
        
        
        lines[indices[0]]= ' '.j..(lines)
        

        lines = [line ___ i,line __ e..(lines) __ i n.. __ indices[1:]]
        


        r.. self





    ___ add_punctuation(self, punctuation: s.., index: i..) __ Document:
        """Add punctuation to the end of a sentence.

        Overwrites existing punctuation.

        Args:
            punctuation (str): The punctuation. One of EOL_PUNCTUATION.
            index (int): The line to change.

        Returns:
            Document: The document with the changed line.
        """

        line = lines[index]
        __ line a.. line[-1] __ EOL_PUNCTUATION:
            line = line[:-1] + punctuation
        ____:
            line += punctuation
        lines[index] = line
        r.. self

    ___ word_count(self) __ i..:
        """Return the total number of words in the document."""
        r.. s..(l..(_remove_punctuation(line).s..()) ___ line __ lines)

    $
    ___ words(self) __ l..:
        """Return a list of unique words, sorted and case insensitive."""
        all_words = set()
        ___ line __ lines:
            line = line.l..
            w = _remove_punctuation(line)
            ___ x __ w.s.. :
                all_words.add(x)

        r.. s..(all_words)




    ___ _remove_punctuation(self,line: s..) __ s..:
        """Remove punctuation from a line."""
        # you can use this function as helper method for
        # Document.word_count() and Document.words
        # or you can totally ignore it
        r.. __.sub(r'[^\w\s]','',line)





    ___ __len__
        """Return the length of the document (i.e. line count)."""
        r.. l..(lines)

    ___ __str__
        """Return the content of the document as string."""
        r.. '\n'.j..(lines)


__ __name__ __ "__main__":
    # this part is only executed when you run the file and is ignored by the tests
    # you can use this section for debugging and testing
    d = (
        Document()
        .add_line("My first sentence.")
        .add_line("My second sentence.")
        .add_line("Introduction", 0)
        .merge_lines([1, 2])
    )

    print(d)
    print(l..(d))
    print(d.word_count())
    print(d.words)
