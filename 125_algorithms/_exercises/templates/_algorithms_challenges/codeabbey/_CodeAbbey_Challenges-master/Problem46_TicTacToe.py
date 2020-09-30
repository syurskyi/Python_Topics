infile = open("prob46.txt")
infile.readline()
data = infile.readlines()
infile.close()

win = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]

___ line __ data:
    moves = line.strip().split(" ")
    x= [int(i) ___ i __ moves __ moves.index(i)%2__0]
    o= [int(i) ___ i __ moves __ moves.index(i)%2__1]
    highest_x = 0
    highest_o = 0
    ___ i __ range(le.(moves)):
        __ i%2 __ 0 :
            ___ j __ win:
                temp_x = [i ___ i __ x __ i __ j]
                __ le.(temp_x) __ 3:
                    highest_x = ma.([moves.index(str(i)) ___ i __ temp_x])
                    break
        ____
            ___ j __ win:
                temp_o = [i ___ i __ o __ i __ j]
                __ le.(temp_o) __ 3:
                    highest_o = ma.([moves.index(str(i)) ___ i __ temp_o])
                    break
                
    __ highest_x __ 0 and highest_o __ 0:
        print("0",end=" ")
    ____ highest_x __0 or highest_o __0:
        print(highest_x+1 __ highest_o__0 else highest_o+1,end= " ")
    ____ highest_x < highest_o:
        print(highest_x+1,end=" ")
    ____
        print(highest_o+1,end=" ")
            
            
    
    
        
