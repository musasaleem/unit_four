# Musa Saleem
# Date: 10/11/18
# Last Modified: 10/11/18
# Comments: In this assignment, I created a simple version of the casino game, blackjack. I made it simple by
# having the dealer only draw two cards and there being no possibility of the Ace card. Another way I made it simple is
# by not having actual gambling be involved. The money factor would make it very complicated as well. I had the user
# and dealer get cards by using the random function and randomizing two cards between one and ten. I then gave the user
# the option to draw another card and if the user did I gave the user the total value of all the cards combined. I then
# drew two random cards for the dealer. Based on how the user and the dealer's cards compare, determined who won the
# game of blackjack

import random


def draw_card():
    return random.randint(1, 10)


def dealer():
    print("The dealer will now draw two cards")
    dealcard1 = draw_card()
    dealcard2 = draw_card()
    print("The Dealers' two cards combined equals", (dealcard1 + dealcard2))
    return dealcard1 + dealcard2


def winner(dealer_total, user_total, name):
    if user_total < dealer_total:
        print("I am sorry,", name, "you lost and the dealer wins this hand")
    elif user_total > dealer_total:
        print("Congratulations", name, "! you won and the dealer lost this hand")
    elif user_total == dealer_total:
        print("Ah shoot, a waste of a hand! Nobody wins...")


def main():
    name = input("what is your name")
    print("Hello", name, "let's play a game of blackjack")
    print("I will now give you two cards")
    card1 = draw_card()
    card2 = draw_card()
    card3 = draw_card()
    user_total = card1 + card2
    print("Your two cards combined equals", (card1 + card2))
    hit_or_stay = input("Would you like to hit or stay")
    if hit_or_stay == "hit":
        print("You drew a", card3)
        user_total = user_total + card3
        print("Your total is now,", user_total)

    if user_total > 21:
        print("I am sorry,", name, ",your total went over 21, you lose this hand")
    else:
        dealer_total = dealer()
        winner(dealer_total, user_total, name)


main()
