import random, os

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

    a_art_1 = " _____\n"
    a_art_2 = "|     |\n"
    a_art_3 = "|  1  |\n"
    a_art_4 = "|     |\n"
    a_art_5 = "|_____|\n"

    b_art_1 = " _____\n"
    b_art_2 = "|     |\n"
    b_art_3 = "|  2  |\n"
    b_art_4 = "|     |\n"
    b_art_5 = "|_____|\n"

    c_art_1 = " _____\n"
    c_art_2 = "|     |\n"
    c_art_3 = "|  3  |\n"
    c_art_4 = "|     |\n"
    c_art_5 = "|_____|\n"


    card1 = a_art_1 + a_art_2 + a_art_3 + a_art_4 + a_art_5
    card2 = b_art_1 + b_art_2 + b_art_3 + b_art_4 + b_art_5
    card3 = c_art_1 + c_art_2 + c_art_3 + c_art_4 + c_art_5

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
