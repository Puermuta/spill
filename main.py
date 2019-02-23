import time
import c
import os

clear = lambda: os.system('cls' or 'clear')

def menu():
    clear()
    print(c.bold + "     Choose a game!")
    print(c.bold + "1." + c.reset + "0 to 50")
    print(c.bold + "2." + c.reset + "lol, nothing here yet...")
    choice = int(input("Write a number to choose: "))
    if choice == 1:
        import guessingGame
        print('Taking you to ' + c.yellow + '0 to 50' + c.reset + '!')
        time.sleep(.25)
        guessingGame.welcome()
    else:
        print(c.red + 'Choose a valid number!', c.reset)
