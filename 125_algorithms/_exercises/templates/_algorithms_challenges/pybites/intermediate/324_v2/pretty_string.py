import pprint
from typing import Any


___ pretty_string(obj: Any) -> str:
    # TODO: your code
    return pprint.pformat(obj, width=60, depth=2)
