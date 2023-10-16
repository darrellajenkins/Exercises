import random

import time

ply_cards = []
dlr_cards = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


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
    remove_ace()
    
    if sum(dlr_cards) == 21 and sum(ply_cards) == 21 or sum(dlr_cards) == 21 and sum(ply_cards) < 21:
        print(f"Your final hand is: {ply_cards[0]} | {ply_cards[1]}, with a final score of {sum(ply_cards)}.\nThe Dealer has Blackjack with cards {dlr_cards[0]} | {dlr_cards[1]}, with a winning score of {sum(dlr_cards)}.\n\nYou lose even if you had Blackjack too! 😒")
        new_game1 = input("\n\tWould you like to play another game of Blackjack? Type 'y' or 'n': ")
        if new_game1 == "y":
            clear()
            time.sleep(1)
            beginning()
        elif new_game1 == "n":
            print("\nHave a nice day and thank you for playing! Come back and play again soon! 😃")
        elif new_game1 != "y" or new_game1 != "n":
            print("\nYou did not enter 'y or n', game will restart in 5 seconds...")
            time.sleep(5)
            beginning()
    elif sum(ply_cards) == 21 and sum(dlr_cards) < 21:
        print(f"Your final hand is: {ply_cards[0]} | {ply_cards[1]}, with a winning score of: {sum(ply_cards)}. 😉\nThe Dealer's final hand is: {dlr_cards[0]} | {dlr_cards[1]} with a final score of {sum(dlr_cards)}.\n\nYou have Blackjack with exactly 21, you win! 🥳🎇🥳🎈🥳🎉")
        new_game2 = input("\n\tWould you like to play another game of Blackjack? Type 'y' or 'n': ").lower()
        if new_game2 == "y":
            clear()
            time.sleep(1)
            beginning()
        elif new_game2 == "n":
            print("\nHave a nice day and thank you for playing! Come back and play again soon! 😃")
        elif new_game2 != "y" or new_game2 != "n":
            print("\nYou did not enter 'y or n', game will restart in 5 seconds...")
            time.sleep(4)
            beginning()
    else:
        print(f"Your cards are {ply_cards[0]} | {ply_cards[1]}, and current score: {sum(ply_cards)}\n")
    print(f"The Dealer's first card is: {dlr_cards[0]}\n")
    game_part2()


def game_part2():
    global cards, ply_cards, dlr_cards
    dontstopgame = True
    while dontstopgame:
        if sum(ply_cards) < 21:
            keep_drawing = input("Would you like another card, 'y or n'?: ").lower()
            if keep_drawing == "n":
                endgame()
            elif keep_drawing == "y":
                ply_cards.append(random.choice(cards))
                if sum(ply_cards) == 21 or sum(dlr_cards) == 21 or sum(ply_cards) > 21:
                    dontstopgame = False
                    print(f"Your cards are {ply_cards[0:]}, and current score: {sum(ply_cards)}\n")
                dlr_draws()
    endgame()

def endgame():
    global cards, ply_cards, dlr_cards, keep_drawing
    keep_drawing = input("Would you like another card, 'y or n'?: ").lower()
    if keep_drawing == "n":
        dlr_draws()
        print("Your cards are:", *ply_cards, sep = ' | ')
        print(f"And your final score is: {sum(ply_cards)}")
        print("The Dealer's cards are:", *dlr_cards, sep = ' | ')
        print(f"And the Dealer's final score is: {sum(dlr_cards)}")
        if sum(ply_cards) > 21 and sum(dlr_cards) > 21:
            return "\nYou busted - you lose."
        elif sum(ply_cards) == sum(dlr_cards):
            return "DRAW"
        elif sum(dlr_cards) == 21:
            return "You lose. The Dealer has 21."
        elif sum(ply_cards) == 21:
            return "You have 21 - you win!!!"
        if sum(ply_cards) > 21:
            return "\nYou busted - you lose."
        if sum(dlr_cards) > 21:
            return "\nThe Dealer went over. You win!!!"
        if sum(ply_cards) > sum(dlr_cards):
            return "You WIN!!!"
    new_game3 = input("\nThank you for playing! Play again 'y or n?: 😃")
    if new_game3 == "y":
        clear()
        time.sleep(1)
        beginning()
    elif new_game3 == "n":
        print("\nHave a nice day and thank you for playing! Come back and play again soon! 😃")
                        
def remove_ace():
    global cards, ply_cards, dlr_cards
    if 11 in ply_cards and sum(ply_cards) > 21:
        ply_cards.remove(11)
        ply_cards.append(1)
    if 11 in dlr_cards and sum(dlr_cards) > 21:
        dlr_cards.remove(11)
        dlr_cards.append(1)
        
def clear() -> None:
    """Clear the terminal."""
    print("\33[H\033[2J" , end="", flush=True)

def dlr_draws():
    global cards, ply_cards, dlr_cards
    while sum(dlr_cards) < 17:
        dlr_cards.append(random.choice(cards))
        remove_ace()
        sum(dlr_cards)
        

def beginning():
    from termcolor import colored
    from art import logo
    clear()
    print(colored(logo,'magenta'))
    print(colored("\t\t\t\t\t\t\tLet's play Blackjack!!!\n\n", 'yellow'))
    game_part1()

beginning()

