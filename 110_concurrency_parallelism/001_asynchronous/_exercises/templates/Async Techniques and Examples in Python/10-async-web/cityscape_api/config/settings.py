? os
? json


___ load(mode='dev') -> dict:
    file = os.path.join(os.path.dirname(__file__), f"{mode}.json")
    if not os.path.exists(file):
        raise Exception(f"Config not found for {mode}.")

    w__ open(file, 'r', encoding='utf-8') __ fin:
        r_ json.load(fin)
