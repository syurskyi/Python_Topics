____ abc _______ ABC, abstractmethod


class Challenge(ABC):
    ___ __init__(self, number, title):
        self.number = number
        self.title = title

    @abstractmethod
    ___ verify(self, _):
        raise TypeError()

    @property
    @abstractmethod
    ___ pretty_title(self):
        raise TypeError()


class BlogChallenge(Challenge):
    ___ __init__(self, number, title, merged_prs):
        super().__init__(number, title)
        self.merged_prs = merged_prs

    ___ verify(self, pr):
        r.. pr __ self.merged_prs

    @property
    ___ pretty_title(self):
        r.. f'PCC{self.number} - {self.title}'


class BiteChallenge(Challenge):
    ___ __init__(self, number, title, result):
        super().__init__(number, title)
        self.result = result

    ___ verify(self, result):
        r.. result __ self.result

    @property
    ___ pretty_title(self):
        r.. f'Bite {self.number}. {self.title}'
