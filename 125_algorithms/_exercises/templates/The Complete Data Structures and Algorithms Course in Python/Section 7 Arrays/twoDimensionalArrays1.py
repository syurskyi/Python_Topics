#   Created by Elshad Karimov on 05/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.


_____ numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ])
print(twoDArray)

# newTwoDArray = np.insert(twoDArray, 1, [[1,2,3,4]], axis=0)
# print(newTwoDArray)

print(le_(twoDArray))

newTwoDArray = np.ap..(twoDArray, [[1,2,3,4]], axis=0)
print(newTwoDArray)
print(le_(newTwoDArray))
print(le_(newTwoDArray[0]))

___ accessElements(array, rowIndex, colIndex
    __ rowIndex >= le_(array) a__ colIndex >= le_(array[0]
        print('Incorrect Index')
    ____
        print(array[rowIndex][colIndex])

accessElements(newTwoDArray, 1, 2)

___ traverseTDArray(array
    ___ i __ ra__(le_(array)):
        ___ j __ ra__(le_(array[0])):
            print(array[i][j])


traverseTDArray(twoDArray)


___ searchTDArray(array, value
    ___ i __ ra__(le_(array)):
        ___ j __ ra__(le_(array[0])):
            __ array[i][j] __ value:
                r_ 'The value is located index '+st.(i)+" "+st.(j)
    r_ 'The element no found'


print(searchTDArray(twoDArray, 444))

newTDArray = np.delete(twoDArray, 1, axis=1)
print(newTDArray)