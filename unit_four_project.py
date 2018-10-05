import random


def main():
    name = input("What is your name?")
    print("Hello", (name), "let's play a game of blackjack")
    print("I will now give you two cards")
    card1 = random.randint(1, 10)
    card2 = random.randint(1, 10)
    print("Your two cards combined equals",(card1 + card2))



def dealer():
    print("The dealer will now draw two cards")
    dealcard1 = random.randint(1, 10)
    dealcard2 = random.randint(1, 10)
    print("The Dealers' two cards combined equals",(dealcard1 + dealcard2))


main()