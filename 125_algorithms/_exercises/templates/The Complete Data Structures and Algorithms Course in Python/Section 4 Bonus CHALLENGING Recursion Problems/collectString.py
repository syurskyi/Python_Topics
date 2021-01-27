#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# collectStrings Solution

___ collectStrings(obj
    resultArr = []
    ___ key __ obj:
        __ type(obj[key]) is str:
            resultArr.append(obj[key])
        __ type(obj[key]) is dict:
            resultArr = resultArr + collectStrings(obj[key])
    r_ resultArr



obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}

print(collectStrings(obj)) # ['foo', 'bar', 'baz'])