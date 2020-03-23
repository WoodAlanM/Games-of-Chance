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




#Call your game of chance functions here
