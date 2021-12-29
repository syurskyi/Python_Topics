____ decimal _______ Decimal
class IntList(l..):


     
    

    @property
    ___ mean(self):
        r.. s..(self)/l..(self)


    @property
    ___ median(self):
        v = s..(self)
        __ l..(v) % 2 __ 1:
            r.. v[l..(v)//2]
        ____:
            r.. (v[l..(v)//2 -1] + v[l..(v)//2])/2




    ___ a..(self,values):

        __ isi..(values,int) o. isi..(values,float) o. isi..(values,Decimal):
            values = float(values)
            super().a..(values)
        ____ isi..(values,l..):
            __ a..(type(v) __ (int,float,Decimal) ___ v __ values):
                self += values
            ____:
                raise TypeError
        ____:
            raise TypeError


    ___ __iadd__(self,value):
        __ isi..(value,l..):
            __ a..(type(v) __ (int,float,Decimal) ___ v __ value):
                ___ v __ value:
                    self.a..(v)
                r.. self
            ____:
                raise TypeError
        ____:
            raise TypeError







    ___ __add__(self,value):
        __ isi..(value,l..):
            __ a..(type(v) __ int ___ v __ value):
                r.. super().__add__(value)
            ____:
                raise TypeError
        ____:
            raise TypeError















