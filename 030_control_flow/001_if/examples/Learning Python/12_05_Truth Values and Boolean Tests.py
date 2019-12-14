__author__ = 'sergejyurskyj'

print('#' * 52 + ' Less-than: return True or False (1 or 0)')
print(2 < 3, 3 < 2)        # Less-than: return True or False (1 or 0)

print('#' * 52 + ' Return left operand if true')
print(2 or 3, 3 or 2)      # Return left operand if true
                 # Else, return right operand (true or false)
print([] or 3)

print([] or {})

print('#' * 52 + ' Return left operand if false')
print(2 and 3, 3 and 2)    # Return left operand if false
                  # Else, return right operand (true or false)
print([] and {})

print(3 and [])
