import os
import poker_move
from colorama import init, Fore, Style
import random
import numpy as np
import time
import poker_ai
init()

cards = np.array(["H_10", "H_9", "H_8", "H_7", "H_6", "H_5", "H_4", "H_3", "H_2", "H_b", "H_d", "H_k", "H_a", "Kr_10", "Kr_9", "Kr_8", "Kr_7", "Kr_6", "Kr_5", "Kr_4", "Kr_3", "Kr_2", "Kr_b", "Kr_d", "Kr_k",
                  "Kr_a", "Ka_10", "Ka_9", "Ka_8", "Ka_7", "Ka_6", "Ka_5", "Ka_4", "Ka_3", "Ka_2", "Ka_b", "Ka_d", "Ka_k", "Ka_a", "P_10", "P_9", "P_8", "P_7", "P_6", "P_5", "P_4", "P_3", "P_2", "P_b", "P_d", "P_k", "P_a"])
rou = 1
card_show = 3
commands = {
    "bet": poker_move.poker_bet(),
    "raise": poker_move.poker_raise(),
    "check": poker_move.poker_check(),
    "fold": poker_move.poker_fold(),
    "all in": poker_move.poker_all_in(),
    "exit": lambda: exit("Bye Bye")
}
comm_cards = []
Player1_cards = []
Ais_cards = [[]]
Ais_coins = [[]]
Player1_coins = {}
pot_coins = 0


def card_gen():

    del comm_cards[:], Player1_cards[:],  # , Player2_cards[:]
    np.random.shuffle(cards)
    ran = random.sample(range(51), 9)

    for i in range(len(ran)):
        if i == 1 or i == 2:
            Player1_cards.append(cards[ran[i]])
        elif i == 3 or i == 4:
            pass
        else:
            comm_cards.append(cards[ran[i]])


run = True
rou_fin = True
game_state = True
os.system("cls")
print("\n\n\n\t\t\t\t\t\t█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
print("\t\t\t\t\t\t█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█")
print("\t\t\t\t\t\t█░░║║║╠─║─║─║║║║║╠─░░█")
print("\t\t\t\t\t\t█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█")
print("\t\t\t\t\t\t█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
play = input("\t\t\t\t\t\t\tPLay\n\n\n\t\t\t\t\t\t\t").lower()

if isinstance(play, str) and play == "p" or play == "play":

    while run:
        number_ai = int(
            input("How many players do you want to play against? (min.1 - max. 9) "))
        if number_ai >= 10 or number_ai < 1:
            print("Sorry that are too many/ less!")
            run = False
            break
        while game_state:
            card_gen()
            while rou_fin:
                os.system("cls")
                print("\n\n\n\n\n\t\t\t\t\t\t\t*  *\n\n\n\n\n\n\n\n\t\t\t\t\t" + str(comm_cards[:card_show]) + "\n\n\t\t\t\t\t\t\t" +
                      str(pot_coins) + "$\n\n\n\t\t\t\t\t\t" + str(Player1_cards) + "\n\n\n\n")
                print("\n\n\n\t\t" + Fore.CYAN +
                      "check\t\tbet\t\traise\t\tfold\t\tall in\t\tcheck\n\n" + Style.RESET_ALL, end="")
                command = input("> ").lower().split(" ")

                if command[0] in commands:
                    commands[command[0]]
                else:
                    print("Sorry this command is not available")

            rou_fin = True
            if not card_show >= 5:
                card_show += 1
            rou += 1
    card_show = 3
