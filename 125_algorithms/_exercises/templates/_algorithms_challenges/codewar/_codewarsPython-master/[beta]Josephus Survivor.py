___ josephus_survivor(n,k
    circle [i ___ i __ r..(1,n+1)]
    index -1
    w.... circle.c.. 0) !_ n-1:
        steps k
        w.... steps > 0:
            __ index + 1 > n-1:
                index 0
                steps -_ 1
            ____ circle[index+1] __ 0:
                index += 1
            ____
                index += 1
                steps -_ 1
        circle[index] 0
        print(circle,index)
    ___ num __ circle:
        __ num !_ 0:
            r.. num
print(josephus_survivor(14,2

#[1,2,3,4,5,6,7] - initial sequence 3
#[1,2,4,5,6,7] => 3 is counted out 6
#[1,2,4,5,7] => 6 is counted out 9 2
#[1,4,5,7] => 2 is counted out 12 5
#[1,4,5] => 7 is counted out 15 
#[1,4] => 5 is counted out
#[4] => 1 is the last element - the survivor!