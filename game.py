import random

cases = ["rock", "paper", "scissors"]
winningCases = [["rock", "scissors"], ["scissors", "paper"], ["paper", "rock"]]
computerPoints = 0
playerPoints = 0

while True:
    try:
        gameDuration = int(input("Please give a count (number of rounds): "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

def play():
    global computerPoints, playerPoints

    for _ in range(gameDuration):
        computer = random.choice(cases)
        player = input("Please choose rock, scissors, or paper (or type 'quit' to exit): ").lower()

        if player == "quit":
            print("Game exited by the player.")
            break

        if player not in cases:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        result = [player, computer]
        
        if result in winningCases:
            print(f"You win this round! Player: {player}, Computer: {computer}")
            playerPoints += 1
        elif player == computer:
            print(f"It's a tie! Player: {player}, Computer: {computer}")
        else:
            print(f"Computer wins this round! Player: {player}, Computer: {computer}")
            computerPoints += 1

play()

print("\nGame Over!")
print(f"Player Points: {playerPoints}")
print(f"Computer Points: {computerPoints}")

if playerPoints > computerPoints:
    print("You are the overall winner!")
elif playerPoints < computerPoints:
    print("Computer is the overall winner!")
else:
    print("It's a tie!")
