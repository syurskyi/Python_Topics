c_ phone(object
    ___  -  
        model _ ''
        color _ 'red'

    ___ call 
        print 'Call'

c_ phone2(phone
    ___  -  
        super(phone2, self). - ()

    ___ sendMail 
        pass

    ___ call 
        __ T..:
            pass
        else:
            super(phone2, self).call()

p _ phone2()
