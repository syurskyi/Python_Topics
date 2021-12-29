____ __future__ _______ annotations
_______ string
_______ re

EOL_PUNCTUATION = ".!?"


class Document:
    ___ __init__(self) -> N..
        # it is up to you how to implement this method
        # feel free to alter this method and its parameters to your liking
        self.lines    # list

    ___ add_line(self, line: str, index: int = N..) -> Document:
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
            self.lines.a..(line)
        ____:
            self.lines.insert(index,line)
        r.. self




    ___ swap_lines(self, index_one: int, index_two: int) -> Document:
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
            self.lines[index_one],self.lines[index_two] = self.lines[index_two],self.lines[index_one]
        except IndexError:
            raise IndexError("Invalid indexes")

        r.. self

    ___ merge_lines(self, indices: l..) -> Document:

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
            lines.a..(self.lines[index].strip())
        
        
        
        self.lines[indices[0]]= ' '.join(lines)
        

        self.lines = [line ___ i,line __ enumerate(self.lines) __ i n.. __ indices[1:]]
        


        r.. self





    ___ add_punctuation(self, punctuation: str, index: int) -> Document:
        """Add punctuation to the end of a sentence.

        Overwrites existing punctuation.

        Args:
            punctuation (str): The punctuation. One of EOL_PUNCTUATION.
            index (int): The line to change.

        Returns:
            Document: The document with the changed line.
        """

        line = self.lines[index]
        __ line and line[-1] __ EOL_PUNCTUATION:
            line = line[:-1] + punctuation
        ____:
            line += punctuation
        self.lines[index] = line
        r.. self

    ___ word_count(self) -> int:
        """Return the total number of words in the document."""
        r.. s..(l..(self._remove_punctuation(line).split()) ___ line __ self.lines)

    @property
    ___ words(self) -> l..:
        """Return a list of unique words, sorted and case insensitive."""
        all_words = set()
        ___ line __ self.lines:
            line = line.lower()
            w = self._remove_punctuation(line)
            ___ x __ w.s.. :
                all_words.add(x)

        r.. s..(all_words)




    ___ _remove_punctuation(self,line: str) -> str:
        """Remove punctuation from a line."""
        # you can use this function as helper method for
        # Document.word_count() and Document.words
        # or you can totally ignore it
        r.. re.sub(r'[^\w\s]','',line)





    ___ __len__(self):
        """Return the length of the document (i.e. line count)."""
        r.. l..(self.lines)

    ___ __str__(self):
        """Return the content of the document as string."""
        r.. '\n'.join(self.lines)


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
