____ decimal _______ Decimal
c_ IntList(l..


     
    

    $
    ___ mean
        r.. s..(self)/l..(self)


    $
    ___ median
        v = s..(self)
        __ l..(v) % 2 __ 1:
            r.. v[l..(v)//2]
        ____
            r.. (v[l..(v)//2 -1] + v[l..(v)//2])/2




    ___ a.. values

        __ isi..(values,i..) o. isi..(values,f__) o. isi..(values,Decimal
            values = f__(values)
            super().a..(values)
        ____ isi..(values,l..
            __ a..(t..(v) __ (i..,f__,Decimal) ___ v __ values
                self += values
            ____
                r.. T..
        ____
            r.. T..


    ___ __iadd__ value
        __ isi..(value,l..
            __ a..(t..(v) __ (i..,f__,Decimal) ___ v __ value
                ___ v __ value:
                    a..(v)
                r.. self
            ____
                r.. T..
        ____
            r.. T..







    ___ __add__ value
        __ isi..(value,l..
            __ a..(t..(v) __ i.. ___ v __ value
                r.. super().__add__(value)
            ____
                r.. T..
        ____
            r.. T..















