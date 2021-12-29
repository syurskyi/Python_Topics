from decimal import Decimal
class IntList(list):


     
    

    @property
    ___ mean(self):
        return sum(self)/len(self)


    @property
    ___ median(self):
        v = sorted(self)
        __ len(v) % 2 == 1:
            return v[len(v)//2]
        else:
            return (v[len(v)//2 -1] + v[len(v)//2])/2




    ___ append(self,values):

        __ isinstance(values,int) or isinstance(values,float) or isinstance(values,Decimal):
            values = float(values)
            super().append(values)
        elif isinstance(values,list):
            __ all(type(v) in (int,float,Decimal) for v in values):
                self += values
            else:
                raise TypeError
        else:
            raise TypeError


    ___ __iadd__(self,value):
        __ isinstance(value,list):
            __ all(type(v) in (int,float,Decimal) for v in value):
                for v in value:
                    self.append(v)
                return self
            else:
                raise TypeError
        else:
            raise TypeError







    ___ __add__(self,value):
        __ isinstance(value,list):
            __ all(type(v) == int for v in value):
                return super().__add__(value)
            else:
                raise TypeError
        else:
            raise TypeError















