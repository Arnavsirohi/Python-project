import random


#INTRODUCTION TO PROGRAM

name = input("Enter your name: ")
print("Welcome " + name)
print("We hope you are ready")
print("TO START LET'S DISCUSS ABOUT THE GAME. IT IS A GUESSING GAME WITH THE COMPUTER.")
print("y for yes to continue")
print("n for no to exit the game")

#RUNNING TRUE TO TAKE CONDTION AGAIN AND AGAIN.......


while True:
    a = input("Enter your response: ")
    if a == 'n':
        print("EXITING.........")
        break  # Exit the loop if the user chooses 'n'
    else:
        print("LET'S START THE GAME............") 
        start_range = int(input("Enter the starting range: "))
        end_range = int(input("Enter the last range: "))
        print("THE RANGE ACCORDING TO YOU IS:", (start_range, end_range))
        print("YOU WILL GET 5 CHANCES")
        print("ENTER YOUR CHOICE " + name)
        
        score = 0  # Initialize score
        for i in range(5):  # Loop runs 5 times, providing 5 chances
            # Move random number generation inside the loop
            choice_comp = random.randint(start_range, end_range)
            
            #TRY FOR GENAERTING RANDOM NUMBER AGAIN AND AGAIN
            try:
                choice_user = int(input("Enter your choice here: "))
                if choice_comp == choice_user:
                    print("Well done! You guessed it correct......")
                    print("Computer's choice was:", choice_comp)
                    score += 1  # Increment score if correct
                else:
                    print("You guessed it wrong..........")
                    print("Computer's choice was:", choice_comp)
            except ValueError:
                print("Please enter a valid number.")

        print(f"Your score against the computer is: {score}")
        print("GAME OVER")
        break  # Exit the loop after the game ends


    



