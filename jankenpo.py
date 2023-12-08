import random

options = ["rock", "paper", "scissors"]

rounds = int(input("How many rounds? "))
user_score=0
computer_score=0
counter = 0

print("User: ", user_score)
print("Computer: ", computer_score)

while counter <= rounds:

    user_choice = input("Choose rock, paper or scissors: ")
    computer_choice = random.choice(options)
    
    print("You chose ", user_choice)
    print("Computer chose ", computer_choice)
    
    if user_choice == computer_choice:
        print("Draw, no score")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        user_score += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
        user_score += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        user_score +=1
    else:
        print("Computer wins!")
        computer_score+=1
    counter+=1

    print(counter)
    print("User: ", user_score)
    print("Computer: ", computer_score)
