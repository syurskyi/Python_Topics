infile = open("prob45.txt")
data  = infile.readlines()
infile.close()
output = ""
___ line in data:
    output += str(line.strip())+" "

data = output.split(" ")[:-1]

cards = []
ranks = ["A", "2", '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
suits = ['C', 'D', 'H', 'S']

___ i in range(4
    ___ j in range(13
        cards.append(str(suits[i])+str(ranks[j]))


___ i in range(le.(data)):
    ran = int(data[i])%52
    # swap the two card
    cards[i],cards[ran] =cards[ran],cards[i]

print(" ".join(cards))
