#! /usr/bin/env python
______ random
______ sys

generated = (str(random.randint(0, 9999)).zfill(4))
print(generated)
totalCount = 0


___ cowAndBulls(counter
    player = (str(input("Please enter your guess between 0000 to 9999: ")).zfill(4))
    cows = 0
    bulls = 0

    ___ i in range(0, 4
        generatedVal = generated[i]
        playersVal = player[i]

        __ generatedVal __ playersVal:
            cows += 1
        ____
            bulls += 1

    # for index, value in enumerate(player
    #     if value in str(player)[index:]:
    #         if value == str(player)[index]:
    #             cows += 1
    #     else:
    #         if value in str(player
    #             bulls += 1

    print("cows: %s,bulls: %s" % (cows, bulls))
    counter += 1

    __ cows __ 4:
        print('You win! The guess was: %s' % generated)
        sys.exit()

    cowAndBulls(counter)


__ __name__ __ '__main__':
    print('Welcome to cows and bulls!\n')
    cowAndBulls(totalCount)
