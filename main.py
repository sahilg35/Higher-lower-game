import random
from art import logo,vs
from replit import clear
from game_data import data

def get_random_account():
  return random.choice(data)

def get_account(account):
  name = account["name"]
  description =  account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}."

def result(guess,count_a,count_b):
  if count_a > count_b:
    return guess == "a"
  else:
    return guess== "b"
  
def game():
  print (logo)
  score = 0
  is_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while is_continue:
    account_a = account_b
    account_b = get_random_account()
    
    while account_a == account_b:
      account_b = get_random_account()
  
    print(f"Compare A: {get_account(account_a)}")
    print (vs)
    print(f"Against B: {get_account(account_b)}")
  
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    count_a = account_a["follower_count"]
    count_b = account_b["follower_count"]
    is_correct = result(guess,count_a,count_b)

    clear()
    print (logo)
  
    if is_correct:
      score +=1
      print(f"You're right! Current score: {score}.")
    else:
      is_continue = False
      print(f"Sorry, that's wrong. Final score: {score}.")

game()