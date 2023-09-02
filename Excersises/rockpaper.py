
import random
userScore = 0
computerScore = 0

while True :
    user = int(input("Rock = 1, Paper = 2, Scissors = 3, Quit = 4\n"))
    computer = random.randint(1,3)


    if user == computer:
        print("You tied")
    elif user == 1 and computer == 2 :
        computerScore += 1
        print("Computer won")
    elif user == 1 and computer == 3 :
        userScore += 1
        print("User won")
    elif user == 2 and computer == 1 :
        userScore += 1
        print("User won")
    elif user == 2 and computer == 3 :
        computerScore += 1
        print("Computer won")
    elif user == 3 and computer == 1 :
        computerScore +=1
        print("Computer won")
    elif user == 3 and computer == 2 :
        userScore += 1
        print("User won")

    print("Current User Score", userScore)
    print("Current Computer Score", computerScore)
