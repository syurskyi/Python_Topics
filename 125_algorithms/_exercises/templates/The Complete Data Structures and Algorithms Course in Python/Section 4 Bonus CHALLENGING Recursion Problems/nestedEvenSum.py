#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# nestedEvenSum Solution

___ nestedEvenSum(obj, sum=0
    ___ key __ obj:
        __ type(obj[key]) __ dict:
            sum += nestedEvenSum(obj[key])
        ____ type(obj[key]) __ in. a__ obj[key]%2__0:
            sum+=obj[key]
    r_ sum



obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": T..,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

print(nestedEvenSum(obj1)) # 6
print(nestedEvenSum(obj2)) # 10