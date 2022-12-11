from art import logo
import random
from replit import clear


def choose_random_card():
    """Pick up a rancom card in deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(deck):
    """Calculate the sum of deck"""
    if 11 in deck and sum(deck) > 21 and len(deck) == 2:
        deck.remove(11)
        deck.append(1)
    if deck[len(deck) - 1] == 11 and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)

    return sum(deck)


def blackjack_game():
    game_continue = True
    while game_continue:
        your_cards = []
        delar_cards = []

        for _ in range(2):
            your_cards.append(choose_random_card())
            delar_cards.append(choose_random_card())

        your_score = com_score = 0

        your_score = calculate_score(your_cards)
        com_score = calculate_score(delar_cards)

        if your_score == 21:
            print("You Win")
            game_continue = False
        elif com_score == 21:
            print("You Lose")
            game_continue = False

        print(f"Your cards : {your_cards}, Current score : {your_score}")
        print(f"Dealrs first card : {delar_cards[0]}")

        while your_score <= 21:
            answer = input("Type 'y' to get another card, Type 'n' to pass : ")
            if answer == 'y':
                your_cards.append(choose_random_card())
                your_score = calculate_score(your_cards)
            elif answer == 'n':
                break
            print(
                f"\nYour final hand : {your_cards}, Final score : {your_score}"
            )

        if com_score < 17:
            delar_cards.append(choose_random_card())
            com_score = calculate_score(delar_cards)

            print(
                f"\nDealer's final hand : {delar_cards}, Final score : {com_score} "
            )

        if your_score == 21 and com_score == 21:
            print("\nYou Lose")
        elif your_score > 21 and com_score <= 21:
            print("\nYou Lose")
        elif your_score <= 21 and com_score > 21:
            print("\nYou Win!")
        elif your_score > 21 and com_score > 21:
            print("\nBurst!")
        else:
            if your_score > com_score:
                print("\nYou Win!")
            elif your_score == com_score:
                print("\nDraw")
            else:
                print("You Lose")

        again = input("\nDo you want to play another game?(Type 'y' or 'n'): ")
        if again == 'y':
            clear()
            blackjack_game()
        else:
            game_continue = False


print(logo)

your_cards = []
delar_cards = []

blackjack_game()
