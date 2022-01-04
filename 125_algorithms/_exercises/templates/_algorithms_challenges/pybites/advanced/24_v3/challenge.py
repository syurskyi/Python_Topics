____ abc _______ ABC, abstractmethod


c_ Challenge(ABC):
    ___ - , number, title):
        number = number
        title = title

    @abstractmethod
    ___ verify(self, _):
        r.. T..()

    $
    @abstractmethod
    ___ pretty_title
        r.. T..()


c_ BlogChallenge(Challenge):
    ___ - , number, title, merged_prs):
        super().__init__(number, title)
        merged_prs = merged_prs

    ___ verify(self, pr):
        r.. pr __ merged_prs

    $
    ___ pretty_title
        r.. f'PCC{number} - {title}'


c_ BiteChallenge(Challenge):
    ___ - , number, title, result):
        super().__init__(number, title)
        result = result

    ___ verify(self, result):
        r.. result __ result

    $
    ___ pretty_title
        r.. f'Bite {number}. {title}'
