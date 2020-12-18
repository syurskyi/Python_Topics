from player import Player
from deck import Deck

# This class represents a card game with its corresponding
# deck, player, and dealer.
class CardGame:

    # A class attribute with the instructions of the game
    instructions = """\n | Welcome to our version of the Blackjack Game |
=================================================================================
The goal is to get as close to 21 as possible, without going over 21. 
Each card has a value and a suit. The values are added for the final result.

The game starts by dealing two cards to the player (you) and to the dealer.            
You are playing against the dealer. On each turn, you must choose if you
would like to take another card or stand to stop the game and see if you won.

The game ends if the total value of the player's hand goes over 21,
and it continues until the player chooses to stand if the total value is below 21.

When the game ends or when the player choose to stand,
the total value of each hand is calculated.  
The value that is closest to 21 without going over it wins the game.
If the values is over 21, the player or dealer automatically lose the game.
=================================================================================
"""

    def __init__(self, deck, player, dealer):
        # The game has its corresponding deck,
        # player, and dealer.
        self.deck = deck
        self.player = player
        self.dealer = dealer

        # When the instance is created,
        # the game starts automatically.
        self.start_game()

    def start_game(self):
        # Print a descriptive message with the instructions
        # of the game.
        print(CardGame.instructions)
        # Keep track of the number of turns during the game.
        turn = 1

        # Shuffle the deck before starting the game.
        self.deck.shuffle()

        # Initially, the player and the dealer draw two cards.
        self.player.draw(self.deck).draw(self.deck)
        self.dealer.draw(self.deck).draw(self.deck)

        # As many times as needed,
        # show the hand of the dealer
        # and show the hand of the player
        # then ask the player if he/she
        # would like to ask for another card
        # or if he/she would like to stand.
        while True:

            print(f"== Turn #{turn} ==")

            print("\nThe Dealer's Hand is:")
            self.dealer.show_hand()

            print("\nYour Hand is:")
            self.player.show_hand()

            if self.player.get_hand_value() > 21:
                print("\nThe total value of your hand is over 21")
                break
            elif self.player.get_hand_value() == 21:
                break
            
            choice = self.ask_choice()
            turn += 1

            if choice == 1:
                self.player.draw(self.deck)
            else:
                break

        # Get the total value of each hand
        player_hand = self.player.get_hand_value()
        print("\nValue - Your Hand:", player_hand)
        
        dealer_hand = self.dealer.get_hand_value()
        print("Value - Dealer's Hand:", dealer_hand)

        # Reveal the hidden card
        print("\nThe dealer's hand was:")
        self.dealer.show_hand(True)

        # Print a descriptive message for the user.
        if player_hand > 21:
            print(f"\nYou lose, {self.player.name}. But don't worry, you can play again.")
        elif dealer_hand > 21 or player_hand == 21 or player_hand > dealer_hand:
            print(f"\nYou win, {self.player.name}! Congratulations.")
        elif player_hand < dealer_hand:
            print(f"\nYou lose, {self.player.name}. But don't worry, you can play again.")
        else:
            print("We have a tie")

    def ask_choice(self):
        # Present the options to the user and return the choice as an integer.
        print("\nWhat do you want to do?")
        print("1 - Ask for another card")
        print("2 - Stand")
        choice = int(input("Please enter your choice (1 or 2) below: \n"))

        if choice == 1 or choice == 2:
            return choice
        else:
            print("The value was not valid. I will assume that you chose to stand.")
            return 2
    
# Create the instances
deck = Deck()
you = Player("Nora") # Replace this with your name
dealer = Player("Dealer")

# Start the game
game = CardGame(deck, you, dealer)
