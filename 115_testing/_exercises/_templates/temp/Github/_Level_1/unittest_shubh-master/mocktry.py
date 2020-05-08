# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 21:42:43 2019

@author: Shubh
"""
import requests
c_ Student:
    
    cal = 3
    ___  -  first,last,age):
        self.fname = first
        self.lname = last
        self.age = age
        
    ___ s_email(self):
        return(self.fname + '.' + self.lname + '@gmail.com')
    
    ___ code(self):
        return(self.fname + self.lname)
        
    
    
    ___ mylinkedin  country):
        r = requests.get(f'https://www.linkedin.com/{country}/{self.code()}')

        if r.ok:
            return r.text
        else:
            return 'Bad Response!'


      
#s1 = Student('shubhabrata','mukherjee',72)
#s2 = Student('sumi','dey',12)
#print(s1.code())
#Student.monthly_schedule('in')


