#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# collectStrings Solution

___ collectStrings(obj
    resultArr = []
    ___ key __ obj:
        __ ty..(obj[key]) __ st.:
            resultArr.ap..(obj[key])
        __ ty..(obj[key]) __ dict:
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