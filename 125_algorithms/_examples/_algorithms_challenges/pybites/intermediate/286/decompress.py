from typing import Dict


def decompress(string: str, table: Dict[str, str]) -> str:


    result = [] 
    for c in string:
        if c in table:
            result.extend(decompress(table[c],table))
        else:
            result.append(c)

    return ''.join(result)









