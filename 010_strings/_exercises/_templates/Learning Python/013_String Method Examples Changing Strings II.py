# print('#' * 52 + ' Slice sections from S')
# S _ 'spammy'
# S _ S 3 + 'xx' + S 5  # Slice sections from S
# print(S)
#
# print('#' * 52 + ' Replace all mm with xx in S')
# S _ 'spammy'
# S _ ?.re.. mm xx  # Replace all mm with xx in S
# print ?
# print aa$bb$cc$dd .re.. $ SPAM
#
# S _ 'xxxxSPAMxxxxSPAMxxxx'
#
# print('#' * 52 + ' Search for position')
# where _ ?.fi.. SPAM  # Search for position
#
# print('#' * 52 + ' Occurs at offset 4')
# print ?  # Occurs at offset 4
# S _ ?  ;where + 'EGGS' + ? where+4);
# print(S)
# S _ 'xxxxSPAMxxxxSPAMxxxx'
#
# print('#' * 52 + ' Replace all')
# print ?.re.. SPAM EGGS  # Replace all
#
# print('#' * 52 + ' Replace one')
# print ?.re.. SPAM EGGS _  # Replace one
#
# S _ 'spammy'
# L _ li.. ?
# print ?
#
# print('#' * 52 + ' Works for lists, not strings')
# L 3 _ 'x'  # Works for lists, not strings
# L 4 _ 'x'
# print L
# S _ ''.jo.. L
# print ?
# print SPAM .jo.. eggs sausage ham toast
