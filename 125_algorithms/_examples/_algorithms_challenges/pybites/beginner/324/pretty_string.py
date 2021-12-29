import pprint
from typing import Any


def pretty_string(obj: Any) -> str:
    # TODO: your code
    pp = pprint.PrettyPrinter(width=60, depth =2)
    return pp.pformat(obj)

#pretty_string([1, [2, [3, [4]]]]) # pp = pprint.PrettyPrinter(depth =2)

#pretty_string([["A"] * 11, ["A"] * 12]) #     pp = pprint.PrettyPrinter(width=60)

pretty_string({
                "font-family": "serif",
                "speak": "none",
                "font-style": "normal",
                "font-weight": "400",
                "font-variant": "normal",
                "text-transform": "none",
                "line-height": "1",
            })