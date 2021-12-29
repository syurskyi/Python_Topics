from typing import Dict


___ decompress(string: str, table: Dict[str, str]) -> str:


    result = [] 
    for c in string:
        __ c in table:
            result.extend(decompress(table[c],table))
        else:
            result.append(c)

    return ''.join(result)









