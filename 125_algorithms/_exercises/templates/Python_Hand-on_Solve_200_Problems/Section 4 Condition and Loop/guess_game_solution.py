# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

______ random

number _ random.r_i..(1,9)
guess _ 0
count _ 0


while guess !_ number an. guess !_ "exit":
    guess _ input("What's your guess?")
    
    __ guess __ "exit":
        break
    
    guess _ in.(guess)
    count +_ 1
    
    __ guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    ____
        print("You got it!")
        print("And it only took you",count,"tries!")


