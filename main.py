###############################
##                            #
##      WEEK 6 HOMEWORK       #
##                            #
##           \o/              #
###############################

# YOUR ASSIGNMENT:
# The game is played against the computer (or the program) which should be running like the following:
# 1. The program asks for user's name 
# 2. Then decides for either `rock`, `paper` or `scissor` randomly for itself
# 3. Then asks for user's choice
# 4. Decides who is the winner for the current round
# 5. The score increases by `one` for the winner of the current round
# 6. The game ends, when one of the players reaches a score higher than 3

# Tasks:
# 1. Find the bugs and make the program work
# 2. Display the winner at the end
# 3. Commit and push your changes, then revise the logic of the game and instead of stopping 
# the program when a player reaches the score of 3, we want to run it only 5 rounds and decide 
# the winner of the game by looking at the scores then. Whoever has the higher score, he/she is the winner. 
# (HINT: you need a new variable to keep track of the number of rounds)


# HINT: If you run into an infinite (never ending) loop, or you just want to end the program,
# you can stop the program by [ctrl] + [c] on terminal
# ------ ADD YOUR CODE BELOW: ------


import random


user_name = input("What's your name?\n")
game_running = True
user_score = 0
computer_score = 0

while game_running == True:
    
    # computer chooses 
    possible_choices = ["rock", "paper", "scissor"]
    computer_choice = random.choice(possible_choices)
    
    # user chooses
    user_choice = input(user_name + ", do yo want to choose rock, paper or scissors?\n")

    print("Computer chose " + computer_choice)
    print(user_name + " chose " + user_choice)

    if user_choice == computer_choice:
        print("It's a tie!") 
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            print("Rock wins!")
            print(user_name + " won this round!")
            user_score += 1
        else:
            print("Paper wins!")
            print("Computer won this round!")
            computer_score += 2
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            print("Scissors win!")
            print(user_name + " won this round!")
            user_score += 1
        else:
            print("Rock wins!")
            print("Computer won this round!")
            computer_score += 1 
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print("Paper wins!")
            print(user_name + " won this round!")
            user_score += 1
        else:
            print("Scissors win!")
            print("Computer won this round!")
            computer_score += 1 
    else:
        print("Invalid input! You have not entered rock, paper or scissors, try again.")
    
    print("Scores")
    print("Computer:" + computer_score)
    print(user_name + ":" + user_score)
    if computer_score >= 3 or user_score >= 3:
        game_running = False
        

         
