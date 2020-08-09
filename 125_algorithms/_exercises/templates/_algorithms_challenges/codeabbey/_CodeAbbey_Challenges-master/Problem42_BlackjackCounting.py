infile = open("prob42.txt")
infile.readline()
data = infile.readlines()
infile.close()



for line in data:
    total = 0
    hand = line.strip().split(" ")
    for card in hand:
        __ card.isdigit(
            total += int(card)
        ____ card in "TJQK":
            total += int(10)
        ____ card __ "A":
            total += int(11)

    count = hand.count("A")
    w___ count > 0 and total>21:
        count-=1
        total -= 10

    __ total<=21:
        print(total ,end=" ")
    ____
        print("Bust",end=" ")
            
