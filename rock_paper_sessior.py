import random
print("Select your choice: \n1. Rock \n2. Paper \n3. Sessor")

player_wins = 0
computer_wins = 0
rounds = 5  
for a in range(rounds):
    print(f"\nround {a+1}")
    i = int(input())
    if i == 1:
     print("You select Rock")

    elif i == 2:
     print("You select Paper")

    elif i == 3:
      print("You select Sessor")

    else:
      print("Invalid choice")

    n = random.randint(1, 3)
    if n == 1:
     print("Computer select Rock")

    elif n == 2:
     print("Computer select Paper")

    elif n == 3:
      print("Computer select Sessor")

    if((i==1 and n==1) or (i==2 and n==2) or (i==3 and n==3)):
     print("Draw Match ")

    elif((i==1 and n==2) or (i==2 and n==3) or (i==3 and n==1)):
     print("You lost the Game, Better luck next time")
     computer_wins += 1

    else:
     print("Congrats, You won the Game")
     player_wins += 1

print("\nGame over!")  
print(f"Final score: you {player_wins}-{computer_wins} computer")

if player_wins > computer_wins:
    print("Congrats! You are the overall winner!")
elif player_wins < computer_wins:
    print("You lost the game. Better luck next time!")
else:
    print("It's a draw!")
   
    


   
  

