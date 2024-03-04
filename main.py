############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
from art import logo
from random import randint
from os import system
import re


def dealer_win(user, comp):
  user['cash'] -= bet
  comp['cash'] += bet
  print(f'Your cash: ${user["cash"]}')
  print(f'Your cards: {user["cards"]}')
  print(f'Dealer cash: ${comp["cash"]}')
  print(f'Dealer cards: {comp["cards"]}')
  print('Dealer win!')


def user_win(user, comp):
  user['cash'] += bet
  comp['cash'] -= bet
  print(f'Your cash: ${user["cash"]}')
  print(f'Your cards: {user["cards"]}')
  print(f'Dealer cash: ${comp["cash"]}')
  print(f'Dealer cards: {comp["cards"]}')
  print('You win!')


def draft(user, comp):
  print(f'Your cash: ${user_state["cash"]}')
  print(f'Your cards: {user_state["cards"]}')
  print(f'Dealer cash: ${comp_state["cash"]}')
  print(f'Dealer cards: {comp_state["cards"]}')
  print('Draft')


def make_wisdom_decision(cards: list) -> bool:
  if sum(cards) < 16:
    return True
  return False


def take_bet():
  num_pattern = re.compile(r'^[\d]+$')
  raw_bet = input('Your bet: $')
  while re.match(num_pattern, raw_bet) == None or int(raw_bet) < 1:
    print("The bet must be a positive integer value. Try again")
    raw_bet = input('Your bet: $')
  return int(raw_bet)


all_cards = []
comp_state = {'cards': [], 'cash': 1000}
user_state = {'cards': [], 'cash': 1000}
play = True

while play and comp_state['cash'] > 0 and user_state['cash'] > 0:
  system('clear')
  print(logo)
  card = randint(2, 11)
  while all_cards.count(card) > 3:
    card = randint(2, 11)
  all_cards.append(card)
  user_state['cards'].append(card)
  card = randint(2, 11)
  while all_cards.count(card) > 3:
    card = randint(2, 11)
  all_cards.append(card)
  user_state['cards'].append(card)
  card = randint(2, 11)
  while all_cards.count(card) > 3:
    card = randint(2, 11)
  all_cards.append(card)
  comp_state['cards'].append(card)
  card = randint(2, 11)
  while all_cards.count(card) > 3:
    card = randint(2, 11)
  all_cards.append(card)
  comp_state['cards'].append(card)
  while make_wisdom_decision(comp_state['cards']):
    card = randint(2, 11)
    while all_cards.count(card) > 3:
      card = randint(2, 11)
    all_cards.append(card)
    comp_state['cards'].append(card)
  while sum(comp_state['cards']) > 21 and 11 in comp_state['cards']:
    comp_state['cards'][comp_state['cards'].index(11)] = 1
    while make_wisdom_decision(comp_state['cards']):
      card = randint(2, 11)
      while all_cards.count(card) > 3:
        card = randint(2, 11)
      all_cards.append(card)
      comp_state['cards'].append(card)
  print(f'Your cards: {user_state["cards"]}')
  print(f'Dealer cards: {comp_state["cards"][0]}')
  bet = take_bet()
  hit = input('Hit or stand (h/s): ')
  while hit == 'h':
    user_state['cards'].append(randint(2, 11))
    while sum(user_state['cards']) > 21 and 11 in user_state['cards']:
      user_state['cards'][user_state['cards'].index(11)] = 1
    if sum(user_state['cards']) > 21:
      dealer_win(user_state, comp_state)
      break
    print(f'Your cards: {user_state["cards"]}')
    print(f'Dealer cards: {comp_state["cards"][0]}')
    hit = input('Hit or stand (h/s): ')
  if abs(21 - sum(user_state["cards"])) < abs(21 - sum(comp_state["cards"]))\
  and sum(user_state["cards"]) <= 21:
    user_win(user_state, comp_state)

  elif abs(21 - sum(user_state["cards"])) > abs(21 - sum(comp_state["cards"]))\
  and sum(comp_state["cards"]) <= 21:
    dealer_win(user_state, comp_state)

  elif sum(user_state['cards']) <= 21 and sum(comp_state['cards']) > 21:
    user_win(user_state, comp_state)

  elif sum(comp_state['cards']) <= 21 and sum(user_state['cards']) > 21:
    dealer_win(user_state, comp_state)

  else:
    draft(user_state, comp_state)
  if comp_state['cash'] <= 0:
    user_win(user_state, comp_state)
    break
  if user_state['cash'] <= 0:
    dealer_win(user_state, comp_state)
    break
  play = input('Deal? ') == 'y'
  user_state['cards'] = []
  comp_state['cards'] = []
  all_cards = []
  system('clear')