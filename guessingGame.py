import time
import os
import c
import random

r = random
clear = lambda: os.system('cls' or 'clear')
turns = [10, 5, 10, 5, 20]
difficulty = ['Easy', 'Medium', 'Hard', 'Hardcore', 'N00b']
max_int = [25, 25, 50, 50, 25]

def welcomeGame():
    clear()
    print(c.menuHeader('GUESSING GAME'))
    time.sleep(.5)
    print(c.menuTitle('Choose a difficulty:'))
    print(c.menuList('1', difficulty[0]))
    print(c.menuList('2', difficulty[1]))
    print(c.menuList('3', difficulty[2]))
    print(c.menuList('4', difficulty[3]))
    print(c.menuList('5', difficulty[4]))
    choice = int(input(''))
    gameMenu(choice)

def gameMenu(choice):
    choice = choice - 1
    clear()
    print(c.menuItem('You chose difficulty ' + c.menuHighlight(difficulty[choice]) + c.yellow + '!'))
    print(c.menuItem('Do you know the rules?'))
    boolean = input('')
    if int(boolean) == 1:
        clear()
        print(c.menuItem('OK, great!'))
        time.sleep(.75)
    else:
        rules(choice)
    print(c.menuItem("Let's start!"))
    game(choice)

def game(choice):
    number = r.randint(0, max_int[choice])
    turnsDone = 0
    turnsLeft = turns[choice] - turnsDone
    guess = input(c.menuItem("Start guessing!\n"))
    while turnsLeft >= 1:
        if int(guess) == number:
            print(c.menuHighlight('You won!') + c.menuItem('\nPlay again?'))
            boolean = input(c.menuItem('1 or 0: '))
            if boolean == str('1'):
                game(choice)
            else:
                import main
                main.menu()
        elif int(guess) > number:
            print(c.menuItem('Lower!'))
            guess = input("")
        elif int(guess) < number:
            print(c.menuItem('Higher!'))
            guess = input("")
        else:
            print(c.menuError("An error has accrued!"))

def rules(choice):
    clear()
    print(c.menuTitle('These are the rules:'))
    print(c.menuList('1', 'You have ' + str(turns[choice]) + ' lives.'))
    print(c.menuList('2', 'You are going to guess a number between ' + c.lightred + '0' + c.yellow + ' and ' + c.lightred + str(max_int[choice]) + c.yellow + '.'))
    input(c.menuItem("Hit enter when you've read through..."))
    return
welcomeGame()
