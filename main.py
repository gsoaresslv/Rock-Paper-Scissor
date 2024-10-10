import random

def main():
    play = True
    #  Welcome message
    print("Welcome to the Rock, Paper, Scissor bot!")
    while play:
        user = input("Make your move: ") # Collecting user input

        #  Turning user input into a integer
        userp = 3
        while userp > 2:
            if user.upper() == "PAPER":
                userp = 0
            elif user.upper() == "SCISSOR":
                userp = 1
            elif user.upper() == "ROCK":
                userp = 2
            else:
                input("Invalid play! Try typing Scissor, Paper or Rock only: ")

        # Making Bot's move
        botp = random.randint(0,2)
        if botp == 0:
            bot = "PAPER"
        if botp == 1:
            bot = "SCISSOR"
        if botp == 2:
            bot = "ROCK"

        #  Comparing player and bot's moves
        if userp == botp: # Draw
            print("You played " + user.upper() + ", I played " + bot + "! It's a Draw!")
        elif userp == botp+1 or userp == botp-2: # User wins
            print("You played " + user.upper() + ", I played " + bot + "! Congratulations! You win!")
        else: # Bot wins
            print("You played " + user.upper() + ", I played " + bot + "! I'm sorry, you lost! Try Again!" )

        #  Asking if the player wants to keep playing
        valid = 0 
        while valid == 0: 
            playstr = input("Do you want to keep playing?: ")
            if playstr.upper() == "YES":
                play = True
                valid+=1
            elif playstr.upper() == "NO":
                play = False
                valid+=1
            else:
                playstr = input("Invalid Answer! Type only Yes or No: ")
    print("Thanks for playing!")

    return 0
if __name__ == "__main__":
    main()