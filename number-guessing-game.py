import random as rand

def guess_number_game():
  print("----- Number Guessing Game -----")

  number_to_guess = rand.randint(1, 100)
  attempts = 0
  max_attempts = 10
  guessed = False
  print("\nI have selected a number between 1 and 100. You have 10 attempts to guess it. Enter (Q/q) for quit the game.\n")

  while attempts < max_attempts and not guessed:
    user_input = input(f"Attempt {attempts + 1}: Enter your guess: ")
    if user_input.lower() == 'q' or user_input.upper() == 'Q':
      print(f"You chose to quit the game. Your number was {number_to_guess}.\n")
      break
    try:
      user_guess = int(user_input)
      attempts += 1
      if user_guess < 1 or user_guess > 100:
        print("Please guess a number within the range of 1 to 100.\n")
        continue
      if user_guess < number_to_guess:
        print("Your number is Too low! Try again.\n")
      elif user_guess > number_to_guess:
        print("Your number is Too high! Try again.\n")
      else:
        guessed = True
        print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.\n")
    except ValueError:
      print("Invalid input. Please enter an integer.\n")
      
  if not guessed and attempts == max_attempts:
    print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.\n")

if __name__ == "__main__":
  guess_number_game()
  print("------Game Over!------\n")