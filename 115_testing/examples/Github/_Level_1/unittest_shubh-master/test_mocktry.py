import unittest
from mocktry import Student
from unittest.mock import patch

class Testmock(unittest.TestCase):
    
    def setUp(self):
        self.s1 = Student('shubhabrata','mukherjee',72)
        self.s2 = Student('sumitra','dey',12)
        print('this is setUp\n')
        
    def tearDown(self):
        print('this is tearDown\n')


    def test_email(self):
        self.assertEqual(self.s1.s_email(),'shubhabrata.mukherjee@gmail.com')
        self.assertEqual(self.s2.s_email(),'sumitra.dey@gmail.com')
        
        
        self.s1.fname = 'satya'
        self.s1.lname = 'bose'
        self.assertEqual(self.s1.s_email(),'satya.bose@gmail.com')
        
        print('this is email method\n')
        
    
    def test_mycode(self):
        self.assertEqual(self.s1.code(),'shubhabratamukherjee')
        self.assertEqual(self.s2.code(),'sumitradey')
        print('this is code method\n')
        
        self.s1.fname = 'mohua'
        self.s1.lname = 'ray'
        self.assertEqual(self.s1.code(),'mohuaray')
        
    def test_mylinkedin(self):
        with patch('mocktry.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Done'

            s = self.s1.mylinkedin('in')
            mocked_get.assert_called_with('https://www.linkedin.com/in/shubhabratamukherjee')
            self.assertEqual(s, 'Done')

            
            s = self.s2.mylinkedin('in')
            mocked_get.assert_called_with('https://www.linkedin.com/in/sumitradey')
            self.assertEqual(s, 'Done')
            
            print('this is the mock function\n')




if __name__ == '__main__':
    unittest.main()