____ collections _______ n..
____ d__ _______ d__

Transaction = n..('Transaction', 'giver points date')
# https://twitter.com/raymondh/status/953173419486359552
Transaction.__new__.__defaults__ = (d__.n..,)


c_ User:


    ___ - ,name):
        name = name
        karma = 0
        fan_names = set()
        points    # list
        _transactions    # list

    

    $
    ___ fans
        r.. l..(fan_names)

    ___ __add__(self,transaction):
        __ isi..(transaction,Transaction):
            
            _transactions.a..(transaction)
            karma += transaction.points
            points.a..(transaction.points)
            fan_names.add(transaction.giver)
    

    ___ __str__
        r.. f"{name} has a karma of {karma} and {fans} fan{'s' __ fans > 1 ____ ''}"
