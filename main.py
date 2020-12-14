import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card() :
  return random.choice(cards)

def calculate_score(cards) :
  score = sum(cards)
  while score > 21 and 11 in cards :
    cards.remove(11)
    cards.append(1)
    score -= 10
  return score

def first_deal(cards) :
  cards.append(deal_card())
  cards.append(deal_card())

def comp_last_moves(comp_hand) :
  score = calculate_score(comp_hand)
  while score <= 16 :
    comp_hand.append(deal_card())
    score = calculate_score(comp_hand)
  return score

def start_rounds(user_hand, computer_hand, min_number_to_quit) :
  comp_score = calculate_score(computer_hand)
  while True :
    user_score = calculate_score(user_hand)
    if min_number_to_quit > 20 :
      print(f"Your cards: {user_hand}, current score: {user_score}")
    if user_score > 21 or comp_score == 21:
      if min_number_to_quit > 20 :
        print(f"Computer cards: {computer_hand} score: {comp_score}")
      return "c"
    if user_score == 21 :
      return "u"
    if min_number_to_quit > 20 :
      print(f"Computer's first card: {computer_hand[0]}")
    if user_score >= min_number_to_quit :
      user_should_deal = 'n'
    else :
      user_should_deal = 'y'
    if min_number_to_quit > 20 :
      user_should_deal = input("Type 'y' to get another card, type anything else to pass: ")
    if user_should_deal == 'y' :
      user_hand.append(deal_card())
    else :
      break
  comp_score = comp_last_moves(computer_hand)
  if min_number_to_quit > 20 :
    print(f"Computer cards: {computer_hand} score: {comp_score}")
  if comp_score > 21 or user_score > comp_score :
    return "u"
  if comp_score > user_score :
    return "c"
  return "d"
    
def startBlackJack(min_number_to_quit) :
  if min_number_to_quit > 20 :
    print(art.logo)
  user_cards = []
  computer_cards = []
  first_deal(user_cards)
  first_deal(computer_cards)
  winner = start_rounds(user_cards, computer_cards, min_number_to_quit)
  if min_number_to_quit > 20 :
    if winner == "u" :
      print("You Won! 😀😀😀")
    if winner == "c" :
      print("You Lost 😪😪😪")
    if winner == "d" :
      print("Draw! 😑")
  return winner

def make_statistics() :
  chances = {}
  trials = 100000
  for score in range (2,21) :
    sum_win = 0;
    sum_draw = 0;
    for trial in range(0,trials) :
      winner = startBlackJack(score)
      if winner == "u" :
        sum_win += 1
      if winner == "d" :
        sum_draw += 1
    chances[score] = [sum_win / trials, sum_draw / trials]
  return chances;

def cal_expectancy(list, bet) :
  chance_win = list[0]
  chance_draw = list[1]
  chance_loose = 1 - chance_win - chance_draw
  return round(chance_win*bet - chance_loose*bet, 2)

def show_statistics(chances) :
  bet = 100
  print("say you bet on 100$")
  print("minimum number to quit\t\texpected profit")
  for score in chances :
    print(f"{score}\t\t\t\t\t\t{cal_expectancy(chances[score],bet)}")

while input("Do you want to play a game of Blackjack? Type 'y' for yes: ") == "y":
  startBlackJack(22)

if input("Do you want statistics about Blackjack? Type 'y' for yes: ") == "y":
  table = make_statistics()
  show_statistics(table)
