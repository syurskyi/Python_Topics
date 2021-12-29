from decimal import Decimal
class IntList(list):


     
    

    @property
    def mean(self):
        return sum(self)/len(self)


    @property
    def median(self):
        v = sorted(self)
        if len(v) % 2 == 1:
            return v[len(v)//2]
        else:
            return (v[len(v)//2 -1] + v[len(v)//2])/2




    def append(self,values):

        if isinstance(values,int) or isinstance(values,float) or isinstance(values,Decimal):
            values = float(values)
            super().append(values)
        elif isinstance(values,list):
            if all(type(v) in (int,float,Decimal) for v in values):
                self += values
            else:
                raise TypeError
        else:
            raise TypeError


    def __iadd__(self,value):
        if isinstance(value,list):
            if all(type(v) in (int,float,Decimal) for v in value):
                for v in value:
                    self.append(v)
                return self
            else:
                raise TypeError
        else:
            raise TypeError







    def __add__(self,value):
        if isinstance(value,list):
            if all(type(v) == int for v in value):
                return super().__add__(value)
            else:
                raise TypeError
        else:
            raise TypeError















