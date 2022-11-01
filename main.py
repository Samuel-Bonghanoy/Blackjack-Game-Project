from blackjack_functions import C_CARDS
from blackjack_functions import P_CARDS
import art
import blackjack_functions
import random
import os
import sys

sufficient_credits = True
#Initializes the token counts of both the player and computer to 1000 and displays it
p_token_count = c_token_count = 1000

while sufficient_credits:
    print(art.logo)

    print("Welcome to Samuel's Blackjack game!\n")
    print(f"Your current token count is {p_token_count}.")

    #Displays the valid values that the user may input and asks them to input their wager until they want to stop
    print(art.money)

    #Initializes the player's wager as 0
    add_wager = 0
    p_cards = [] #empty list to hold the player cards
    c_cards = [] #empty list to hold the computer cards

    #Calls the function and returns the values to these variables
    retry, p_wager = blackjack_functions.wager(p_token_count, add_wager) 
    # #Allows the user to retry wagering if their wager was invalid
    while retry == True:
        if p_wager == True:
            blackjack_functions.wager(p_token_count, add_wager)
        else:
            retry = False

    #Gives the computer and the player two random cards each
    p_card1 = random.choice(art.cards_list)
    p_card2 = random.choice(art.cards_list)
    c_card1 = random.choice(art.cards_list)
    c_card2 = random.choice(art.cards_list)
    c_card_value = art.card_values[c_card1] + art.card_values[c_card2]

    #Displays the player's cards and value of the cards
    blackjack_functions.display_p_cards(p_card1, p_card2)

    #This allows the player to draw cards
    p_card_value, p_cards = blackjack_functions.draw_card(p_card1, p_card2)
    #Displays the player's cards and value of the cards

    new_c_card_value, c_cards = blackjack_functions.computer_draw(p_card_value, c_card_value, c_card1, c_card2)

    #displays the computer's cards and hand value
    blackjack_functions.display_c_cards(c_cards)

    #compares the value of the player's hand to the computer's hand
    result = ""
    result = blackjack_functions.compare(p_card_value, new_c_card_value)

    #applies wager increase or decrease to user
    if result == "win":
        p_token_count += p_wager
        print(f"You won and your current token count is {p_token_count}!")

    elif result == "lose":
        p_token_count -= p_wager
        print(f"You lost, and your current token count is {p_token_count}.")

    #ends program if user does not have sufficient tokens to wager
    if not p_token_count >= 25:
        sufficient_credits =  False
        print("You do not have sufficient tokens to continue playing. Thank you for playing!")
        break

    #asks user if he wants to go again
    go_again = input("Do you want to play again? Type 'y' for yes or 'n' to exit: ").lower()

    if go_again == "y":
        sufficient_credits == True
    elif go_again == "n": 
        sufficient_credits == False
        print("Thank you for playing!")
        break

    os.system('cls||clear')
    
