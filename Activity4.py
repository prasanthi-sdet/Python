# Get the users names
user1 = input("What is Player 1's name? ")
user2 = input("What is Player 2's name? ")

while True:
    # Get the users choices
    user1_answer = input(user1 + ", do you want to choose rock, paper or scissors? ").lower()
    user2_answer = input(user2 + ", do you want to choose rock, paper or scissors? ").lower()
    if(user1_answer not in ('rock','paper','scissors') or user2_answer not in ('rock','paper','scissors')):
        print("Invalid input! You have not entered rock, paper or scissors, try again.")
    elif user1_answer == user2_answer:
        print("It's a tie!")
    elif user1_answer == 'rock':
        if user2_answer == 'scissors':
            print("Rock wins!")
        else:
            print("Paper wins!")
    elif user1_answer == 'scissors':
        if user2_answer == 'paper':
            print("Scissors win!")
        else:
            print("Rock wins!")
    elif user1_answer == 'paper':
        if user2_answer == 'rock':
            print("Paper wins!")
        else:
            print("Scissors win!")            
    anotherround_input=input("Do you want to play another round Yes/No: ").lower()
    if(anotherround_input=="yes"):
        continue
    elif(anotherround_input=="no"):
        break
    else:
        print("Invalid input, Game is exiting now")
        raise SystemExit
