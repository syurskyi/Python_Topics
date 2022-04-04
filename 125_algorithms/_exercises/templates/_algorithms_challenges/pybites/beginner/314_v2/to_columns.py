____ t___ _______ List  # not needed when we upgrade to 3.9
_______ m__

___ print_names_to_columns(names: List[s..], cols: i.. = 2) __ N..

    
    rows = i..(m__.ceil(l..(names) / cols))

    
    ___ row __ r..(rows
        ___ col __ r..(cols
            index = row * cols + col
            ___
                name  = names[index]
            ______ I..
                _____
            print _*| {name:<10}',end='')
        ____:
            print()
            _____
        _____






__ _______ __ _______
    

    names =  "Bob Julian Tim Sara Eva Ana Jake Maria".s..

    print_names_to_columns(names,cols=3)








