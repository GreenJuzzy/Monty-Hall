import random
import os


def game():
    os.system("cls")

    correctCard = random.randint(1, 3)

    # Start - Ascii Art

    m1 = """  
              __  __             _           _    _       _ _ 
             |  \/  |           | |         | |  | |     | | |
             | \  / | ___  _ __ | |_ _   _  | |__| | __ _| | |
             | |\/| |/ _ \| '_ \| __| | | | |  __  |/ _` | | |
             | |  | | (_) | | | | |_| |_| | | |  | | (_| | | |
             |_|  |_|\___/|_| |_|\__|\__, | |_|  |_|\__,_|_|_|
                                      __/ |                   
                                     |___/                    """

    print(m1)
    print("\n\n\n")

    card1 = """     _____
    |     |
    |  1  |
    |     |
    |_____|"""

    card2 = """     _____
    |     |
    |  2  |
    |     |
    |_____|"""

    card3 = """     _____
    |     |
    |  3  |
    |     |
    |_____|"""

    # End - Ascii Art

    print(card1)
    print(card2)
    print(card3)

    print("\nChoose a card.")

    chosenCard = int(input())

    remove = random.randint(1, 3)

    while remove == correctCard or remove == chosenCard:
        remove = random.randint(1, 3)

    Left = ""

    removedCard = card1

    if remove == 1:
        removedCard = card1
        card1 = card1.replace("1", " ")
        Left = "card 2 or 3"

    if remove == 2:
        removedCard = card2
        card2 = card2.replace("2", " ")
        Left = "card 1 or 3"

    if remove == 3:
        removedCard = card3
        card3 = card3.replace("3", " ")
        Left = "card 1 or 2"

    os.system("cls")
    print("-----\nI removed card {}.\n-----\n\n".format(remove))
    print(" ")
    print(card1)
    print(card2)
    print(card3)

    print("You can choose between {}.".format(Left))

    chosenCard_2 = int(input())

    if chosenCard_2 == correctCard:
        os.system("cls")
        print("\nCorrect, card {} was the right one.\n\n\n".format(correctCard))
    else:
        os.system("cls")
        print("\nWrong, correct card was {}.\n\n\n".format(correctCard))

    restart = input("\n\nWould you like to restart the game?\n> ")
    if restart == "Y" or restart == "y":
        game()

    else:
        0


game()
