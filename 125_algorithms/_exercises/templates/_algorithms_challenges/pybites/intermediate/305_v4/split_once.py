from typing import List
import string


___ split_once(text: str, separators: str = None) -> List[str]:
    print(f'{text=}')
    __ separators is None:
        separators = string.whitespace


    indices = [text.index(sep) for sep in separators __ sep in text]

    __ indices:
        indices = sorted(indices)
        split = []
        last_index = 0
        for index in indices:
            split.append(text[last_index:index])
            last_index = index + 1
        split.append(text[last_index:])
        return split
    else:
        return [text]
