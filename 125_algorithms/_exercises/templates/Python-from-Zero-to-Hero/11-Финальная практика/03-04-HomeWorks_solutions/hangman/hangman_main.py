____ hangman.game _______ Game
____ hangman.game_status _______ GameStatus


___ chars_list_to_str(chars):
    r.. ''.j..(chars)


game  Game()
word  game.generate_word()

letters_count  l..(word)

print(f"The word consists of {letters_count} letters.")
print("Try to guess the word letter by letter.")

w___ game.game_status __ GameStatus.IN_PROGRESS:
    letter  input("Pick a letter.\n")
    state  game.guess_letter(letter)
    print(chars_list_to_str(state))

    print(f"Remaining tries = {game.remaining_tries}")
    print(f"Tried letters: {chars_list_to_str(game.tried_letters)}")

__ game.game_status __ GameStatus.LOST:
    print("You're hanged!")
    print(f"The word was: {game.word}")
____:
    print("Congratulations! You won!")
