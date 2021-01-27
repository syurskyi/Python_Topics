#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# stringifyNumbers Solution

___ stringifyNumbers(obj
    newObj = obj
    ___ key __ newObj:
        __ type(newObj[key]) __ in.:
            newObj[key] = st.(newObj[key])
        __ type(newObj[key]) __ dict:
            newObj[key] = stringifyNumbers(newObj[key])
    r_ newObj



obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": T..,
      "random": 66
    }
  }
}

print(stringifyNumbers(obj))

{'num': '1', 
 'test': [], 
 'data': {'val': '4', 
          'info': {'isRight': T.., 'random': '66'}
          }
}