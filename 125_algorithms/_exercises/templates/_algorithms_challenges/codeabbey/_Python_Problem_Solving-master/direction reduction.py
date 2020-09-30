#accepting the directions from the user
direction = list(map(str, input().split()))
#Modifying the directions to uppercase
direction = [x.upper() ___ x __ direction]

#defining the definition of the direction reduction
___ dirReduc(dir =   # list
    #traversing through all the elements of the list
    ___ j __ range(le.(dir)):
        #traversing through all the elements except the last one
        ___ i __ range(0,le.(dir)-1
            __ dir[i] __ 'NORTH' and dir[i+1] __ 'SOUTH' or dir[i] __ 'SOUTH' and dir[i+1] __ 'NORTH':
                dir.pop(i)
                dir.pop(i)  
                break
            ____ dir[i] __ 'WEST' and dir[i+1] __ 'EAST' or dir[i] __ 'EAST' and dir[i+1] __ 'WEST':
                dir.pop(i)
                dir.pop(i)
                break
            ____
                pass
    #print the result of the direction reduction
    print(dir)
#calling the direction reduciton function
dirReduc(direction)

#north south south east west north west