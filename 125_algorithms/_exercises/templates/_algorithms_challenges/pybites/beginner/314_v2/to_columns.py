____ typing _______ List  # not needed when we upgrade to 3.9
_______ math

___ print_names_to_columns(names: List[str], cols: int = 2) -> N..

    
    rows = int(math.ceil(l..(names) / cols))

    
    ___ row __ r..(rows):
        ___ col __ r..(cols):
            index = row * cols + col
            try:
                name  = names[index]
            except IndexError:
                break
            print(f'| {name:<10}',end='')
        ____:
            print()
            continue
        break






__ __name__ __ "__main__":
    

    names =  "Bob Julian Tim Sara Eva Ana Jake Maria".s..

    print_names_to_columns(names,cols=3)








