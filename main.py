
import random 
from art import logo

def compare(user_nm, comp_nm):
  if user_nm > comp_nm:
    print("Too high.")
    return guesses - 1
  elif user_nm < comp_nm:
    print("Too low.")
    return guesses - 1
  else: 
    print(f"You got it! The answer was {user_nm}")
    exit()

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number= random.choice(range(1,101))
mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if mode == 'easy':
  guesses = 10
elif mode == 'hard':
  guesses = 5


while guesses > 0:
  print(f"\nYou have {guesses} attempts remaining to guess the number.")
  user_guess = int(input("Make a guess: "))
  guesses = compare(user_guess,number)
  print("Guess again.")
else:
  print(f"You lose. The number was {number}.")

  
  
  
  
