import random

def draw_card():
    return random.randint(1, 10)

def dealer():
    print("The dealer will now draw two cards")
    dealcard1 = draw_card()
    dealcard2 = draw_card()
    print("The Dealers' two cards combined equals", (dealcard1 + dealcard2))
    return dealcard1 + dealcard2


def winner(dealer, player):



def main():
    name = input("What is your name?")
    print("Hello", (name), "let's play a game of blackjack")
    print("I will now give you two cards")
    card1 = draw_card()
    card2 = draw_card()
    card3 = draw_card()
    user_total = card1 + card2
    user_total_hit = user_total + card3
    print("Your two cards combined equals", (card1 + card2))
    hit_or_stay = input("Would you like to hit or stay")
    if hit_or_stay == "hit":
        print("You drew a", (card3))
        print("Your total is now,", user_total_hit)

    if user_total_hit > 21:
        print("u lose")
    else:
        dealer_total = dealer()
        winner(dealer_total, user_total)

    if user_total or user_total_hit < dealer_total:
        print("I am sorry, you lost and the dealer wins this hand")
    elif user_total or user_total_hit > dealer_total:
        print("Congratulations! you won and the dealer lost this hand")
    elif user_total_hit or user_total is dealer_total:
        print("Ah shoot, a waste of a hand! Nobody wins...")
    elif user_total or user_total_hit >= 21:
        print("You lost, your hand was over 21")


main()
