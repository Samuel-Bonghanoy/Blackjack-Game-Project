import random
import art
import sys
import os

P_CARDS = []
C_CARDS = []

def wager(p_token_count , wager): #This function handles all the wagering in the game
    wants_to_wager = True
    wager_temp = wager
    add_wager = 0 #Represents the player's initial wager amount
    p_wager = 0 #initializes the player's overall wager as 0
    c_wager = 0 #initializes computer wager as 0 
    while wants_to_wager: #This loop adds the user's additional wager to their overall wager
        if p_token_count > 25:
            wager = int(input("Pick a value to wager: \n"))
            if p_token_count >= wager and p_token_count - wager >= 0 : #Makes sure that the user does not wager more than his current tokens
                if wager == 25 or wager == 50 or wager == 100 or wager == 500 or wager == 1000 : #Makes sure that the user input is a valid wager among the choices
                    p_wager += wager
                    c_wager = p_wager
                    p_token_count -= wager
                    print(f"\nYou just wagered {wager}, and your current token count is {p_token_count}.\n")
                    print(art.money_art[str(wager)])
                    print(f"Your current wager amount is {p_wager}. The computer is forced to wager {c_wager} as well.")
                    wager = 0
                    #Asks the user if they want to wager more
                    restart_choice = input("Do you want to continue? Type 'y' for yes or 'n' to proceed to the game: ").lower()
                    if restart_choice == "y":
                        wants_to_wager = True
                    else:
                        wants_to_wager = False
                        return False, p_wager;
                else: 
                    print("Invalid wager.")
                    #Asks the user if they want to wager more
                    restart_choice = input("Do you want to retry? Type 'y' for yes or 'n' to end the game: ").lower()
                    if restart_choice == "y":
                        wants_to_wager = True
                    else:
                        wants_to_wager = False
                        sys.exit()
                        return False, p_wager;
            else:
                print("Invalid Input: Wager is higher than current token count. Please try again.")
                wager = wager_temp
                restart_choice = input("Do you want to retry? Type 'y' for yes or 'n' to end the game: ").lower()
                if restart_choice == "y":
                    wants_to_wager = True
                else:
                    sys.exit()
        else:
            print("\nYou do not have sufficient tokens, so the game will proceed.")
            return False, p_wager;

def display_p_cards(card1, card2): #Displays the cards that the player has drawn
    print("Your hand is: ")
    print(art.cards_art[card1])
    print(art.cards_art[card2])
    print(f"The value of your hand is currently {art.card_values[card1] + art.card_values[card2]}.")

def display_c_cards(c_card_list): #Displays the cards that the computer has drawn
    new_value = 0
    print("The Computer's hand is: ")
    for card in c_card_list:
            new_value += art.card_values[card]
            print(art.cards_art[card])
    print(f"The value of the computer's hand is currently {new_value}.")

def ace_value(p_value, p_cards):
    # only let this trigger if the value of cards other than ace is > 10
    temp_value = p_value
    # print(p_value)
    # if p_value + art.card_values["ace"] > 21:
    #     for i in range(0, len(p_cards) - 1):
    #         if p_cards[i] == "ace":
    #             p_cards[i] = "ace_11value"
    # elif p_value - 1 > 10:
    #     return
    if p_value == 21 and len(p_cards) == 2:
        return
    if "ace" in p_cards and p_value > 21:
        for i in range(0, len(p_cards) - 1):
            if p_cards[i] == "ace":
                 p_cards[i] = "ace_11value"
        return 

def draw_card(card1, card2): #This function handles the card drawing done in the game
    P_CARDS = [card1, card2]
    value = 0
    new_value = 0
    choice = input("Do you want to draw another card? Type 'y' for yes or 'n' to continue with your current hand: ").lower()
    if choice == "y":
        draw_choice = True
        while draw_choice:
            value = 0
            new_card = random.choice(art.cards_list)
            for card in P_CARDS:
                value += art.card_values[card]
                ace_value(value, P_CARDS)
            if new_card == "ace" and value > 10:
                new_card = "ace_11value"
            value = 0
            P_CARDS.append(new_card)
            for card in P_CARDS:
                value += art.card_values[card]
                ace_value(value, P_CARDS)
                new_value = value
            for card in P_CARDS:
                print(art.cards_art[card])
            # if new_value == 21:
            #     print(f"The value of your hand is currently {new_value}.")
            # elif new_value > 21:
            #     print(f"The value of your hand is currently {new_value}.")
            # else:
            print(f"The value of your hand is currently {new_value}.")

            go_again = input("Do you want to draw again? Type 'y' for yes or 'n' to continue with your current cards: ").lower() #asks the user if they want to draw another card

            if go_again == "y":
                draw_choice = True
            else:
                draw_choice = False
                return new_value, P_CARDS
    else:
        for card in P_CARDS:
                value += art.card_values[card]
        print(f"Your final card value is {value}.")
        return value, P_CARDS

def compare(p_value, c_value):
    if int(p_value) == int(c_value):
        print("Tie.")
        return "tie"

    if int(c_value) > 21 and int(p_value) < 21:
        print("You win.")
        return "win"

    if int(p_value) > int(c_value) and int(p_value) < 21:
        print("Tie.")
        return "tie"

    if int(p_value) == 21 and not int(c_value) == 21:
        print("You win.")
        return "win"

    if int(c_value) > int(p_value) and int(c_value) < 21:
        print("You lose.")
        return "lose"
    
    if int(c_value) == 21 and not int(p_value) == 21:
        print("You lose.")
        return "lose"

    elif int(p_value) > 21:
        # display_c_cards(card1, card2)
        print("You lose.")
        return "lose"

def computer_draw(p_value, c_value, c_card1, c_card2):
    draw = True
    value = 0
    new_value = 0
    holder = 0
    C_CARDS = [c_card1, c_card2]
    if p_value > 21:
        return c_value, C_CARDS
    if c_value < p_value and c_value < 21:
        while draw:
            for card in C_CARDS:
                value += art.card_values[card]
                ace_value(value, C_CARDS)
            if value >= 21:
                draw = False
                break
            new_card = random.choice(art.cards_list)
            if new_card == "ace" and value > 10:
                new_card = "ace_11value"
            C_CARDS.append(new_card)
            if value < 21 and value < p_value:
                draw = True
                value = 0
            if value >= 21:
                draw = False
                value = 0
                break
            if value > p_value:
                draw = False
                value = 0
                break
        for card in C_CARDS:
            new_value += art.card_values[card]
        holder = new_value
        if new_value == 21:
            print(f"The value of the computer's is currently {new_value}.")
            return holder, C_CARDS
        elif new_value > 21:
            print(f"The value of the computer's hand is currently {new_value}.")
            return holder, C_CARDS
        else:
            print(f"The value of the computer's hand is currently {new_value}.")
            return holder, C_CARDS
    else:
        return c_value, C_CARDS