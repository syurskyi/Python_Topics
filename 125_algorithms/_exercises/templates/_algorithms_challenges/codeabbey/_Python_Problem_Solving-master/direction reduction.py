#accepting the directions from the user
direction = l..(map(str, input().split()))
#Modifying the directions to uppercase
direction = [x.upper() ___ x __ direction]

#defining the definition of the direction reduction
___ dirReduc(dir    # list):
    #traversing through all the elements of the list
    ___ j __ r..(l..(dir)):
        #traversing through all the elements except the last one
        ___ i __ r..(0,l..(dir)-1):
            __ dir[i] __ 'NORTH' and dir[i+1] __ 'SOUTH' o. dir[i] __ 'SOUTH' and dir[i+1] __ 'NORTH':
                dir.pop(i)
                dir.pop(i)  
                break
            ____ dir[i] __ 'WEST' and dir[i+1] __ 'EAST' o. dir[i] __ 'EAST' and dir[i+1] __ 'WEST':
                dir.pop(i)
                dir.pop(i)
                break
            ____:
                pass
    #print the result of the direction reduction
    print(dir)
#calling the direction reduciton function
dirReduc(direction)

#north south south east west north west