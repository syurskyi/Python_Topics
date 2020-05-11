# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 21:42:43 2019

@author: Shubh
"""
______ requests
c_ Student:
    
    cal _ 3
    ___  -  first,last,age
        fname _ first
        lname _ last
        age _ age
        
    ___ s_email
        r_(fname + '.' + lname + '@gmail.com')
    
    ___ code
        r_(fname + lname)
        
    
    
    ___ mylinkedin  country
        r _ requests.get(f'https://www.linkedin.com/{country}/{code()}')

        __ r.ok:
            r_ r.text
        ____:
            r_ 'Bad Response!'


      
#s1 = Student('shubhabrata','mukherjee',72)
#s2 = Student('sumi','dey',12)
#print(s1.code())
#Student.monthly_schedule('in')


