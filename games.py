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




#Call your game of chance functions here
