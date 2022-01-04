#accepting the directions from the user
direction = l..(map(s.., input().s..()))
#Modifying the directions to uppercase
direction = [x.u.. ___ x __ direction]

#defining the definition of the direction reduction
___ dirReduc(dir    # list):
    #traversing through all the elements of the list
    ___ j __ r..(l..(dir)):
        #traversing through all the elements except the last one
        ___ i __ r..(0,l..(dir)-1):
            __ dir[i] __ 'NORTH' a.. dir[i+1] __ 'SOUTH' o. dir[i] __ 'SOUTH' a.. dir[i+1] __ 'NORTH':
                dir.pop(i)
                dir.pop(i)  
                break
            ____ dir[i] __ 'WEST' a.. dir[i+1] __ 'EAST' o. dir[i] __ 'EAST' a.. dir[i+1] __ 'WEST':
                dir.pop(i)
                dir.pop(i)
                break
            ____:
                p..
    #print the result of the direction reduction
    print(dir)
#calling the direction reduciton function
dirReduc(direction)

#north south south east west north west