#! /urs/bin/env python
______ random

__ __name__ __ '__main__':
    number = random.randint(0,9)
    attempts = 0

    w___ True:
        player = (raw_input('Guess the number from 0 to 9: '))
        __ player __ 'exit':
            break
        player = int(player)
        attempts+=1

        __ player __ number:
            print('Conrates! You guessed!\n')
            break
        ____ player != number:
            __ number > player:
                print('To low!\n')
            ____
                print('To high!\n')


    print('Number of attempts: %s. Bye!'%attempts )