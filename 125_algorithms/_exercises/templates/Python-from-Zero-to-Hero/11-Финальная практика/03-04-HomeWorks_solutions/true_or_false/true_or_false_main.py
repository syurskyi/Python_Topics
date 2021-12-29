____ true_or_false.game _______ Game
____ true_or_false.game_result _______ GameResult
____ true_or_false.game_status _______ GameStatus


___ end_of_game_handler(result: GameResult):
    print(f"Questions asked:{result.questions_passed}. Mistakes made:{result.mistakes_made}.")
    print("You won!" __ result.won ____ "You lost!")


game  Game("data\\Questions.csv", 3, end_of_game_handler)

w___ game.game_status __ GameStatus.IN_PROGRESS:
    q  game.get_next_question()
    print("Do you believe in the next statement or question? Enter 'y' or 'n'")

    print(q.text)

    answer  input() __ "y"

    __ q.is_true __ answer:
        print("Good job! You're right!")
    ____:
        print("Oops, actually you're mistaken. Here is the commentary:")
        print(q.explanation)

    game.give_answer(answer)

