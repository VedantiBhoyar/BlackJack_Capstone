import  random
from art import logo

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def check_score(card_list):
    total = sum(card_list)
    if total == 21 and len(card_list) == 2:
        return 0
    while 11 in card_list and total>21 :
        card_list.remove(11)
        card_list.append(1)
        total=sum(card_list)
    return total

def compare(user_sum, computer_sum):
    if user_sum == computer_sum:
        return "Draw 🙃"
    if computer_sum == 0:
        return "You lose, dealer has Blackjack 😱"
    if user_sum == 0:
        return "You win with Blackjack 😎"
    if user_sum > 21:
        return "You went over 21. You lose 😭"
    if computer_sum > 21:
        return "Dealer went over 21. You win 😁"
    return "You win 😃" if user_sum > computer_sum else "You lose 😤"


def play_game():
    user_cards = [deal_cards(), deal_cards()]
    computer_cards = [deal_cards(), deal_cards()]
    user_score = check_score(user_cards)
    computer_score = check_score(computer_cards)
    print(f"User cards {user_cards} , Score: {user_score}")
    print(f"Computer first card {computer_cards[0]}")

    game_over = False
    while not game_over:
        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_over = True
        next_run = input("Do you want to get another card\nType y or n")
        if next_run == "y":
            user_cards.append(deal_cards())
            user_score = check_score(user_cards)
            game_over = True
        else:
            while computer_score < 17 and computer_score != 0:
                computer_cards.append(deal_cards())
                computer_score = check_score(computer_cards)
            game_over = True
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play BlackJack\nType y or n").lower() == "y":
    print("\n"*20)
    print(logo)
    play_game()





