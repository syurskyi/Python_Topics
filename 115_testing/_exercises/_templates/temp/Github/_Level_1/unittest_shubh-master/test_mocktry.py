______ unittest
____ mocktry ______ Student
____ unittest.mock ______ patch

c_ Testmock(unittest.TestCase):
    
    ___ setUp
        s1 _ Student('shubhabrata','mukherjee',72)
        s2 _ Student('sumitra','dey',12)
        print('this is setUp\n')
        
    ___ tearDown
        print('this is tearDown\n')


    ___ test_email
        assertEqual(s1.s_email(),'shubhabrata.mukherjee@gmail.com')
        assertEqual(s2.s_email(),'sumitra.dey@gmail.com')
        
        
        s1.fname _ 'satya'
        s1.lname _ 'bose'
        assertEqual(s1.s_email(),'satya.bose@gmail.com')
        
        print('this is email method\n')
        
    
    ___ test_mycode
        assertEqual(s1.code(),'shubhabratamukherjee')
        assertEqual(s2.code(),'sumitradey')
        print('this is code method\n')
        
        s1.fname _ 'mohua'
        s1.lname _ 'ray'
        assertEqual(s1.code(),'mohuaray')
        
    ___ test_mylinkedin
        with patch('mocktry.requests.get') as mocked_get:
            mocked_get.return_value.ok _ True
            mocked_get.return_value.text _ 'Done'

            s _ s1.mylinkedin('in')
            mocked_get.assert_called_with('https://www.linkedin.com/in/shubhabratamukherjee')
            assertEqual(s, 'Done')

            
            s _ s2.mylinkedin('in')
            mocked_get.assert_called_with('https://www.linkedin.com/in/sumitradey')
            assertEqual(s, 'Done')
            
            print('this is the mock function\n')




if __name__ == '__main__':
    unittest.main()