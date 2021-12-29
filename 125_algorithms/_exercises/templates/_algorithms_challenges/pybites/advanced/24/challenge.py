from abc import ABC, abstractmethod


class Challenge(ABC):


    ___ __init__(self,number,title):
        self.number = number
        self.title = title

    @abstractmethod
    ___ verify(self,other):
        pass


    @property
    @abstractmethod
    ___ pretty_title(self):
        pass


class BlogChallenge(Challenge):


    ___ __init__(self,number,title,merged_prs):
        super().__init__(number,title)
        self.merged_prs = merged_prs
    
    

    ___ verify(self,other):
        return other in self.merged_prs
    
    @property
    ___ pretty_title(self):
        return f"PCC{self.number} - {self.title}"

class BiteChallenge(Challenge):

    ___ __init__(self,number,title,result):
        super().__init__(number,title)
        self.result = result
    

    ___ verify(self,other):
        return other == self.result

    @property
    ___ pretty_title(self):
        return f"Bite {self.number}. {self.title}"

