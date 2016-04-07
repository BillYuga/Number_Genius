#Guess the number game.

import random

#menu function
def menu():
    print ("\n\n+----------------------------+")
    print ("|            MENU            |")
    print ("+----------------------------+")
    print ("| 1: Play game               |")
    print ("| 2: Review points           |")
    print ("| 3: Reset                   |")
    print ("| 4: How to play             |")
    print ("| 5: About game              |")
    print ("| 6: Exit                    |")
    print ("+----------------------------+")
    choice = raw_input("Enter your choice:")
    print ("+----------------------------+")

    while choice not in ('1','2','3', '4', '5', '6'):
        print ("Invalid choice!")
        choice = raw_input("Enter choice again:")
    return choice

#Level_choice function
def level_choice():
    print ("+----------------------------+")
    print ("|      Select a level:       |")
    print ("+----------------------------+")
    print ("|\t1: Easy (1-10)       |")
    print ("|\t2: Normal (1-15)     |")
    print ("|\t3: Hard (1-25)       |")
    print ("+----------------------------+")
    level = raw_input("Enter level:")
    while level not in ('1','2','3'):
        print ("Level does not exist!")
        level = input("Enter another level:")
    return level

#check user's guess
def check_guess():
    global guess, rand_num, lives, win, win_points, games_won
    while not guess.isdigit():
        print ("Value must be  a number!")
        print ("+----------------------------+")
        guess = raw_input("What is your guess:")
    while lives >= 0 and win == False:
           
        if int(guess) == rand_num:
            if lives == 2:
                win_points += 3
            elif lives == 1:
                win_points += 2
            else :
                win_points += 1
            print ("+----------------------------+")
            print ("Congratulations!!! You win.")
            print ("Lives left:", lives)
            print ("+----------------------------+")
            
            win = True
            games_won += 1
        elif lives == 0: #and guess != rand_num:
            print ("Lives left:", lives)
            print ("You loose!! \nGame over")
            print ("The number was:", rand_num)
            break
        elif int(guess) > rand_num:
            print ("+----------------------------+")
            print ("Too high")
            lives -= 1
            print ("Lives left:", lives + 1)
            print ("+----------------------------+")
            guess = raw_input("guess again:")
        elif int(guess) < rand_num:
            print ("+----------------------------+")
            print ("Too low")
            lives -= 1
            print ("Lives left:", lives + 1)
            print ("+----------------------------+")
            guess = raw_input("guess again:")
        
            
#main game play function
def play_game():
    global lives, win, rand_num, guess, games_won, games_played
    lives = 2
    win = False
    menu_choice = menu()
    if menu_choice == '1':
        games_played += 1
        level_ = level_choice()
        if level_ == '1':
            rand_num = random.randint(1,10)
            guess = raw_input("What is your guess")
            check_guess()
        elif level_ == '2':
            rand_num = random.randint(1,15)
            print ("What is your guess")
            guess = raw_input()
            check_guess()
        else:
            rand_num = random.randint(1,25)
            print ("What is your guess")
            guess = raw_input()
            check_guess()
    elif menu_choice == '2':
        print ("+----------------------------+")
        print ("| Games played:", games_played,"           |")
        print ("+----------------------------+")
        print ("| Games won:", games_won, "              |")
        print ("+----------------------------+")
        print ("| Games lost:", games_played - games_won, "             |")
        print ("+----------------------------+")
        print ("| Score:", win_points, "                  |")
        print ("+----------------------------+")
    elif menu_choice == '3':
        reset()
    elif menu_choice == '4':
        print ("+----------------------------+")
        print ("+-----------PLAYING-----------")
        print ("| The computer chooses a     |")
        print ("| based on the level you     |")
        print ("| specify in the gameplay.   |")
        print ("| You are then given three   |")
        print ("| to guess the number.       |")
        print ("+-----------SCORING-----------")
        print ("| If you get the right number|")
        print ("| on your first attempt, you |")
        print ("| gain 3 pts. If you get the |")
        print ("| right number on your second|")
        print ("| attempt, you gain 2 pts.   |")
        print ("| If you get the right number|")
        print ("| on your last attempt, you  |")
        print ("| gain 1 pt.                 |")
        print ("+----------------------------+")
    elif menu_choice == '5':
        print ("+----------------------------+")
        print ("|          MATH GENIUS       |")
        print ("| Release date:   23/03/2016 |")
        print ("| Release time:     11:33 PM |")
        print ("| Developer:      Fosam Bill |")
        print ("| Asisted:        SHU RAMISH |")
        print ("| Development time:    7 Hrs |")
        print ("+----------------------------+")
        
    else:
        print ("+--------------------------------------+")
        print ("| Thanks for playing the game...       |")
        print ("| We'll be glad to have you back. Bye! |")
        print ("+--------------------------------------+")
        return 0
    play_game()

#reset game values
def reset():
    global win_points, games_won, games_played
    win_points = 0
    games_won = 0
    games_played = 0
    print ("+----------------------------+")
    print ("|    Reset successful!!!     |")
    print ("+----------------------------+")
        
print ("+*******NUMBER GENIUS********+")
print ("+****************************+")
win_points = 0
games_won = 0
games_played = 0
play_game()



    



