import pprint
from typing import Any


___ pretty_string(obj: Any) -> str:
    pp = pprint.pformat(obj, depth=2, width=60)
    return pp