from random import choice

# Ask the players about their names
player_1 = input("Player 1, Please enter your name: ")
player_2 = input("player 2, Please Enter Your Name: ")
play = True
# While loop to rerun the game
while play:
    game = list(range(0, 9))
    # A boolean variable to detect a winner
    win = False
    # A counter to count how many times the players played
    occupied_cases = 0
    # Choose the player X and the player O
    player_turn = choice([player_1, player_2])
    if player_turn == player_1:
        print(player_1, "You are player 'X',", player_2, "You are player 'O'")
    else:
        print(player_2, "You are player 'X',", player_1, "You are player 'O'")
    while not win and occupied_cases <= 8:
        # Print the map and ask the first player to play
        print("\n" + str(game[0]), game[1], game[2])
        print(game[3], game[4], game[5])
        print(game[6], game[7], game[8], "\n")
        move = int(input("Player 'X', make a move: "))
        while move not in range(0, 9) or game[move] not in range(0, 9):
            move = int(input("Invalid input make a new move: "))
        game[move] = "X"
        # Print the map again to see the changes after the first player played
        print("\n" + str(game[0]), game[1], game[2])
        print(game[3], game[4], game[5])
        print(game[6], game[7], game[8], "\n")
        occupied_cases += 1
        win = (game[0]) == game[1] == game[2] or game[3] == game[4] == game[5] or game[6] == game[7] == game[8] or \
              game[0] == game[3] == game[6] or game[1] == game[4] == game[7] or game[2] == game[5] == game[8] or \
              game[0] == game[4] == game[8] or game[2] == game[4] == game[6]
        if win:
            print("\n***Player X won!***")
            play_again = input("You wanna play again?(y=Yes/n=No): ").lower()
            while play_again != 'y' and play_again != 'n':
                play_again = input("Invalid input, You wanna play again?(y=Yes/n=No): ").lower()
                play = play_again == 'y'
                if play:
                    print("\n***New Game!***\n")
        elif occupied_cases > 8:
            print("\n***Draw, Game Over!***")
            play_again = input("You wanna play again?(y=Yes/n=No): ").lower()
            while play_again != 'y' and play_again != 'n':
                play_again = input("Invalid input, You wanna play again?(y=Yes/n=no): ").lower()
                play = play_again == 'y'
                if play:
                    print("\n***New Game!***\n")
        else:
            move = int(input("Player '0', make a move: "))
            print("\n" + str(game[0]), game[1], game[2])
            print(game[3], game[4], game[5])
            print(game[6], game[7], game[8], "\n")
            while move not in range(0, 9) or game[move] not in range(0, 9):
                move = int(input("Invalid input, make a new move: "))
            game[move] = "0"
            occupied_cases += 1
            win = game[0] == game[1] == game[2] or game[3] == game[4] == game[5] or game[6] == \
                  game[7] == game[8] or game[0] == game[3] == game[6] or game[1] == game[4] == game[
                      7] or game[2] == game[5] == game[8] or game[0] == game[4] == game[8] or game[
                      2] == game[4] == game[6]
            if win:
                print("\n***Player 'O' won!***")
                play_again = input("You wanna play again? (y=Yes/n=No): ").lower()
                while play_again != 'y' and play_again != 'n':
                    play_again = input("Invalid input, You wanna play again? (y=Yes/n=No): ").lower()
                    play = play_again == 'y'
                    if play:
                        print("\n***New Game!***\n")
