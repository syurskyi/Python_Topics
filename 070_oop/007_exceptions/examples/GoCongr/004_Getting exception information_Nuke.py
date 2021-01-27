try:
    x = 1 / 0                     
except (NameError, IndexError, ZeroDivisionError) as err:
    print(err.__class__.__name__) 
    print(err)
    nuke.critical(str(err))