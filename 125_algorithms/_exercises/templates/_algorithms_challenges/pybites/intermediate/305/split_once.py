from typing import List
import string


___ split_once(text: str, separators: str = None) -> List[str]:

    __ separators == None:
        separators = string.whitespace 

    separators= set(separators)
    result = []
    previous_start = 0
    for i,c in enumerate(text):
        __ c in separators:
            result.append(text[previous_start:i])
            previous_start = i + 1
            separators.remove(c)

    result.append(text[previous_start:])        
    return result



__ __name__ == "__main__":

    print(split_once('abc: def: ijk, lmno: pqr - stu, wxy', separators=',-:'))

