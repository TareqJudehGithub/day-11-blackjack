############### Blackjack Project #####################
from random import choice
from time import sleep
from replit import clear
from art import logo



def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = choice(cards)
  return card

# Calculating cards total:
def calculate_score(cards):
  ''' Take a list of cards, and return the score calculated'''
  score = sum(cards)
  if score == 21 and len(cards) == 2:
      return 0

  if score > 21 and 11 in cards:  
    cards.remove(11)
    cards.append(1)
  return score

  
def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "You lose, opponent has Blackjack!"
  elif user_score == 0:
    return "Win with a Blackjack!"
  elif user_score > 21:
    return "you went over.. you lose!"
  elif computer_score > 21:
    return "Opponent went over. You win!"
  elif user_score > computer_score:
    return "You win!"
  else:
    return "You lose!"

def play_game():

  print(logo)

  user_cards = []
  computer_cards = []
  is_game_over = False

  # Drawing cards for user and for computer:
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print("")
    sleep(1)
   
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer first card: {computer_cards[0]}")
    print("")
    sleep(1)

    if user_score == 0 or computer_score == 0 or user_score > 21:
      print("Game Over!")
      is_game_over = True
    else:
      user_should_deal =  input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True
  print("")
  sleep(1)
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
    
  print(f"your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
  
  print("")
  sleep(1)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()


