try:                           
    x = 1 / 0                  
except ZeroDivisionError:      
    nuke.critical('Not possible to divide 0')
    x = 0
print(x) 