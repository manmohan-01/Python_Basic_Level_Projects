print("Enter Your choices:-")
print("r for Rock")
print("p for Paper")
print("s for scissors")

import random
computer = random.choice([-1,0,1])
yourstr = input("\nEnter your choice : ")
youDict = {
  "r": 1,
  "p": 0,
  "s": -1
}
reverseDict = {
  1: "Rock",
  0: "Paper",
  -1: "Scissors"
}
player = youDict[yourstr]

print(f"You choose {reverseDict[player]}\nComputer choose {reverseDict[computer]}")

if(computer == 1):
  if (player == 1):
    print("Match is Tie!")
  elif(player == 0):
    print("You Win")
  elif(player == -1):
    print("You Loose")

elif(computer == 0):
  if (player == 1):
    print("You Loose")
  elif(player == 0):
    print("Match is Tie!")
  elif(player == -1):
    print("You Win")

elif(computer == -1):
  if (player == 1):
    print("You Win")
  elif(player == 0):
    print("You Losse")
  elif(player == -1):
    print("Match is Tie!")

else:
  print("Enter your correct choice!")
