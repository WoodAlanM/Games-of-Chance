import random

money = 100

#Coin flip function
#Compares input from the player to the coin flip
#and returns the amount of money won or lost
def coin_flip(bet, player_guess):
    num = random.randint(1, 2)
    if player_guess == "Heads" and num == 1:
        return bet
    else:
        return bet * -1

#Print to test the function
#print(coin_flip(50, "Heads"))

#Cho Han function
#Simulates rolling two dice
#Player picks odd or even
#Function compares players choice to the roll
#and return the amount of money won or lost
def cho_han(bet, odd_even):
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)
    sum_of_roll = roll_one + roll_two
    if sum_of_roll % 2 == 0 and odd_even == "Even":
        return bet
    else:
        return bet * -1

#Print to test the function
#print(cho_han(50, "Even"))

#52 Card pick two game
#Simulates two cards being picked the higher of the two wins
#Function pics two cards and compares their value
#Returns the amount of money won or lost
deck = [11,11,11,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,
        9,9,9,9,8,8,8,8,7,7,7,7,6,6,6,6,5,5,5,5,4,4,4,4,3,3,3,3,2,2,2,2]

def pick_two_cards(bet):
    card1_value = 0
    card2_value = 0
    new_deck = []
    num1 = random.randint(1, 52)
    num2 = random.randint(1, 51)
    card1_value = deck[num1]
    print(card1_value)
    print(deck)
    for index in range(52):
        if index != num1 - 1:
            new_deck.append(deck[index])
        else:
            continue
    card2_value = new_deck[num2]
    print(new_deck)
    print(card2_value)

    #check the card values to see who won
    if card1_value > card2_value:
        return bet
    elif card1_value == card2_value:
        return 0
    else:
        return bet * -1

#Print to test the function
#print(pick_two_cards(50))









#Call your game of chance functions here
