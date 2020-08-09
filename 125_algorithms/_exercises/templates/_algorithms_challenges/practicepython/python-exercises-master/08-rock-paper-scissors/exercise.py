#! /urs/bin/env python
______ random

__ __name__ __ '__main__':
    options = ['rock','paper','scissors']

    w___ True:
        player = str(raw_input('You choice(rock, paper, scissors '))
        opponent = str(options[random.randint(0,2)])

        __ player __ options[0] and opponent __ options[2]:
            print('Conrates! You won! (%s,%s)'%(player, opponent))
            break
        ____ player __ options[1] and opponent __ options[0]:
            print('Conrates! You won!(%s,%s)'%(player, opponent))
            break
        ____ player __ options[2] and opponent __ options[1]:
            print('Conrates! You won!(%s,%s)'%(player, opponent))
            break
        ____ player __ opponent:
            print("It's a draw! Try again. (%s,%s)"%(player, opponent))
            break
        ____
            print('You loose :/ Try again! (%s,%s)'%(player, opponent))
            break