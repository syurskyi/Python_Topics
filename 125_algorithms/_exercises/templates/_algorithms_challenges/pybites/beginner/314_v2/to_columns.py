from typing import List  # not needed when we upgrade to 3.9
import math

___ print_names_to_columns(names: List[str], cols: int = 2) -> None:

    
    rows = int(math.ceil(len(names) / cols))

    
    for row in range(rows):
        for col in range(cols):
            index = row * cols + col
            try:
                name  = names[index]
            except IndexError:
                break
            print(f'| {name:<10}',end='')
        else:
            print()
            continue
        break






__ __name__ == "__main__":
    

    names =  "Bob Julian Tim Sara Eva Ana Jake Maria".split()

    print_names_to_columns(names,cols=3)








