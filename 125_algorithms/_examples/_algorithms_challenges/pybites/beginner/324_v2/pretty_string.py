import pprint
from typing import Any


def pretty_string(obj: Any) -> str:
    # TODO: your code
    

    pp = pprint.PrettyPrinter(width=60,depth=2,sort_dicts=True)
    return pp.pformat(obj)
