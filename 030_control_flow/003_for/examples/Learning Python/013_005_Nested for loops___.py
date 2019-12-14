__author__ = 'sergejyurskyj'



items = ["aaa", 111, (4, 5), 2.01]   # A set of objects
tests = [(4, 5), 3.14]               # Keys to search for

print('#' * 52 + ' For all keys')
print('#' * 52 + ' For all items')
print('#' * 52 + ' Check for match')
for key in tests:                    # For all keys
    for item in items:               # For all items
        if item == key:              # Check for match
            print(key, "was found")
            break
    else:
        print(key, "not found!")

print('#' * 52 + ' For all keys')
print('#' * 52 + ' Let Python check for a match')
for key in tests:                    # For all keys
    if key in items:                 # Let Python check for a match
        print(key, "was found")
    else:
        print(key, "not found!")


print('#' * 52 + ' Start empty')
print('#' * 52 + ' Scan first sequence')
print('#' * 52 + ' Common item?')
print('#' * 52 + ' Add to result end')
seq1 = "spam"
seq2 = "scam"
res = []                             # Start empty
for x in seq1:                       # Scan first sequence
    if x in seq2:                    # Common item?
        res.append(x)                # Add to result end
print(res)


print('#' * 52 + ' Let Python collect results')
print([x for x in seq1 if x in seq2]) # Let Python collect results
