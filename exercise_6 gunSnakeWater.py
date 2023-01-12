# Snake water gun
# Create a snake water gun game in Python! Search Snake water gun game in google if you need help on rules and how to play the game!

# gun>snake , snake>water , water>gun
# 3>1         1>2              2>3
import random


def randomnumber():
    return random.randint(1, 3)


# 1 - snake , 2 - water , 3 - gun
print("Welcome to snake water gun game !")

lis = ["snake", "water", "gun"]

while True:
    yourScore = 0
    computerScore = 0
    i = 0
    while True:
        print(f"Your current score {yourScore}   Computer current score {computerScore}")
        print(f"You have left life {5 - i}\n")
        print("Enter : 1 for Snake\n2 for water\n3 for gun")
        yourNumber = int(input())
        if yourNumber > 3:
            print("you enter wrong choice")
            continue
        comNum = randomnumber()
        print(f"Computer choice is {lis[comNum - 1]}")
        if comNum == 1 and yourNumber == 3:
            yourScore += 1
        elif comNum == 2 and yourNumber == 1:
            yourScore += 1
        elif comNum == 3 and yourNumber == 2:
            yourScore += 1
        elif comNum == yourNumber:
            print("OOPS! Your choice is same\nplease try again")
        else:
            computerScore += 1
        if i == 5:
            break
        i += 1

    if yourScore > computerScore:
        print("\nCongratulation! You win the game!")
    elif yourScore == computerScore:
        print("\nMatch draw!")
    else:
        print("\nComputer Win!")
    print("Play Again ?\ny for YES , n for NO")
    choice = input()
    if choice == 'n':
        break
