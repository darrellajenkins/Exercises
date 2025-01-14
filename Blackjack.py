import random
import time
import os


# My blackjack solution October 2023.

logo = """\033[35m
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \\  /|K /\\  |     | '_ \\| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \\/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
      |  \\/ K|                            _/ |                
      `------'                           |__/           
"""

ply_cards = []
dlr_cards = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def playover():
    global cards, ply_cards, dlr_cards
    ply_cards = []
    dlr_cards = []
    new_game3 = input("\nThank you for playing! Play again 'y or n?: 😃 ")
    if new_game3 == "y":
        time.sleep(1)
        clear()
        beginning()
    elif new_game3 == "n":
        print("\nHave a nice day and thank you for playing! Come back and play again soon! 😃")
    elif new_game3 != "y" or new_game3 != "n":
        print("You did not enter 'y or n', please try again: ")
        playover()
        
def game_part1():
    time.sleep(1)
    global cards, ply_cards, dlr_cards
    plyr_card1 = random.choice(cards)
    plyr_card2 = random.choice(cards)
    ply_cards.append(plyr_card1)
    ply_cards.append(plyr_card2)

    dealer_card1 = random.choice(cards)
    dealer_card2 = random.choice(cards)
    dlr_cards.append(dealer_card1)
    dlr_cards.append(dealer_card2)
    remove_ace_ply()
    remove_ace_dlr()
    
    if sum(dlr_cards) == 21 and sum(ply_cards) == 21 or sum(dlr_cards) == 21 and sum(ply_cards) < 21:
        print(f"Your final hand is: {ply_cards[0]} | {ply_cards[1]}, with a final score of {sum(ply_cards)}.\nThe Dealer has Blackjack with cards {dlr_cards[0]} | {dlr_cards[1]}, with a winning score of {sum(dlr_cards)}.\n\nYou lose even if you had Blackjack too! 😒")
        new_game1 = input("\n\tWould you like to play another game of Blackjack? Type 'y' or 'n': ")
        if new_game1 == "y":
            ply_cards = []
            dlr_cards = []
            time.sleep(1)
            beginning()
        elif new_game1 == "n":
            print("\nHave a nice day and thank you for playing! Come back and play again soon! 😃")
        elif new_game1 != "y" or new_game1 != "n":
            print("\nYou did not enter 'y or n', game will restart in 5 seconds...")
            ply_cards = []
            dlr_cards = []
            time.sleep(4)
            beginning()
    elif sum(ply_cards) == 21 and sum(dlr_cards) < 21:
        print(f"Your final hand is: {ply_cards[0]} | {ply_cards[1]}, with a winning score of: {sum(ply_cards)}. 😉\nThe Dealer's final hand is: {dlr_cards[0]} | {dlr_cards[1]} with a final score of {sum(dlr_cards)}.\n\nYou have Blackjack with exactly 21, you win! 🥳🎇🥳🎈🥳🎉")
        new_game2 = input("\n\tWould you like to play another game of Blackjack? Type 'y' or 'n': ").lower()
        if new_game2 == "y":
            ply_cards = []
            dlr_cards = []
            time.sleep(1)
            beginning()
        elif new_game2 == "n":
            print("\nHave a nice day and thank you for playing! Come back and play again soon! 😃")
        elif new_game2 != "y" or new_game2 != "n":
            print("\nYou did not enter 'y or n', game will restart in 5 seconds...")
            ply_cards = []
            dlr_cards = []
            time.sleep(4)
            beginning()
    else:
        print(f"Your cards are {ply_cards[0]} | {ply_cards[1]} and current score: {sum(ply_cards)}\n")
        print(f"The Dealer's first card is: {dlr_cards[0]}\n")
        game_part2()

def game_part2():
    go = True
    while go:
        keep_drawing = input("Would you like another card, 'y or n'?: ").lower()
        for chk in keep_drawing:
            if keep_drawing == "y" and sum(ply_cards) < 21:
                ply_cards.append(random.choice(cards))
                remove_ace_ply()
                print("Your cards are:", *ply_cards, sep=' | ')
                print(f"And your score is: {sum(ply_cards)}\n")
                if sum(ply_cards) < 21:
                    game_part2()
                else:
                    endgame()
            if keep_drawing == "n":
                print("Your cards are:", *ply_cards, sep=' | ')
                print(f"And your score is: {sum(ply_cards)}\n")
                go = False
                endgame()
            else:
                go = False

def endgame():
    global cards, ply_cards, dlr_cards
    dlr_draws()
    print("The Dealer's cards are:", *dlr_cards, sep = ' | ')
    print(f"And the Dealer's final score is: {sum(dlr_cards)}")
    if sum(ply_cards) > 21 and sum(dlr_cards) > 21:
        print("\nYou busted - you lose.")
        playover() 
    elif sum(ply_cards) == sum(dlr_cards):
        print("DRAW")
        playover() 
    elif sum(dlr_cards) == 21:
        print("You lose. The Dealer has 21.")
        playover() 
    elif sum(ply_cards) == 21:
        print("You have 21 - you win!!!")
        playover() 
    elif sum(ply_cards) > 21:
        print("\nYou busted - you lose.")
        playover() 
    elif sum(dlr_cards) > 21:
        print("\nThe Dealer went over. You win!!!")
        playover() 
    elif sum(ply_cards) > sum(dlr_cards):
        print("You WIN!!!")
        playover() 
    elif sum(ply_cards) > sum(dlr_cards) and sum(dlr_cards) < 21:
        print("\nYou WIN!!!")
        playover() 
    if sum(dlr_cards) > sum(ply_cards) and sum(dlr_cards) <= 21:
        print("\nYou lose - Dealer wins.")
        playover() 
    else:
        return "You lose."
        playover()    
                        
def remove_ace_dlr():
    global cards, ply_cards, dlr_cards
    if 11 in dlr_cards and sum(dlr_cards) > 21:
        dlr_cards.remove(11)
        dlr_cards.append(1)

def remove_ace_ply():
    global cards, ply_cards, dlr_cards
    if 11 in ply_cards and sum(ply_cards) > 21:
        ply_cards.remove(11)
        ply_cards.append(1)
        
def clear() -> None:
    """Clear the terminal."""
    print("\33[H\033[2J" , end="", flush=True)
    os.system("cls")
    
def dlr_draws():
    global cards, ply_cards, dlr_cards
    while sum(dlr_cards) < 17:
        dlr_cards.append(random.choice(cards))
        remove_ace_dlr()
        sum(dlr_cards)
        
def beginning():
    clear()
    print(f"\033[34m\t\t\t\t\t\t\tLet's play Blackjack!!!\n\n{logo}\033[33m")
    game_part1()

beginning()


