______ u__
____ mocktry ______ Student
____ u__.m.. ______ patch

c_ Testmock?.?
    
    ___ setUp
        s1 _ Student('shubhabrata','mukherjee',72)
        s2 _ Student('sumitra','dey',12)
        print('this is setUp\n')
        
    ___ tearDown
        print('this is tearDown\n')


    ___ test_email
        aE..(s1.s_email(),'shubhabrata.mukherjee@gmail.com')
        aE..(s2.s_email(),'sumitra.dey@gmail.com')
        
        
        s1.fname _ 'satya'
        s1.lname _ 'bose'
        aE..(s1.s_email(),'satya.bose@gmail.com')
        
        print('this is email method\n')
        
    
    ___ test_mycode
        aE..(s1.code(),'shubhabratamukherjee')
        aE..(s2.code(),'sumitradey')
        print('this is code method\n')
        
        s1.fname _ 'mohua'
        s1.lname _ 'ray'
        aE..(s1.code(),'mohuaray')
        
    ___ test_mylinkedin
        w__ patch('mocktry.requests.get') __ mocked_get:
            mocked_get.return_value.ok _ T..
            mocked_get.return_value.text _ 'Done'

            s _ s1.mylinkedin('in')
            mocked_get.a_c_w..('https://www.linkedin.com/in/shubhabratamukherjee')
            aE..(s, 'Done')

            
            s _ s2.mylinkedin('in')
            mocked_get.a_c_w..('https://www.linkedin.com/in/sumitradey')
            aE..(s, 'Done')
            
            print('this is the mock function\n')




__ _____ __ _____
    ?.?