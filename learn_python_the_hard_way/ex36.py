'''
This script is a simple clone of Zork
It's nothing fancy but it shows how well I grasped the basics of the python language
'''
from sys import exit


def lines():
    '''
    This does nothing but prints lines to make things look pretty (well I think they will look pretty)
    '''
    print('\n')
    print('-' * 75)
    print('\n')


def start():
    '''
    The game starts from this scene. pretty simple
    '''
    lines()
    print('You wake up to find yourself in front of an old house.')
    print('You\'re leg is tied to a chian that leads inside the house.')
    print('You find a saw next to you.')
    print('Do you follow the chain or saw your foot off?\n')

    while True:
        choice = input('>')

        if 'follow' in choice:
            print('\n')
            main_hall()
        elif 'saw' in choice:
            dead('You die from the pain.')
        else:
            print('That makes no sense\n')


def dead(sentence):
    '''
    This is the death scene
    '''
    print('\n')
    print(sentence, ' Good job!\n')
    lines()
    exit(0)


def main_hall():
    '''
    The first room the player sees when they enter the house
    '''
    lines()
    print('You enter a large dark hall.\nYou look around in the dark using only the light comming from oustide\nand manage to see that there are 2 doors other than the one you came from\nThe door on your right says \'DO NOT ENTER\'\nand the door on your left says \'ENTER IF YOU DARE\'\nYou also see that the chain around your foot is tied to the ground here\nbut you can\'t seem to figure out how to unlock the chain from your foot\nWhich door do you choose?\n')

    while True:
        choice = input('>')

        if 'left' in choice:
            gold_room()
        elif 'right' in choice:
            cthulhu_room()
        elif 'back' in choice:
            back_out()
        else:
            print('\n')
            print('This is no time to act stupid, just make up your mind')
            print('\n')


def cthulhu_room():
    print('Here you see the great evil Cthulhu.')
    print('He, it, whatever stares at you and you go insane.')
    print('Do you flee for your life or eat your head?')

    choice = input('>')

    if 'flee' in choice:
        start()
    elif 'head' in choice:
        dead('Well that was tasty!')
    else:
        cthulhu_room()


def gold_room():
    print('You enter a room full of gold!\nWith a sign on top that says take as much as you want,\nBUT NOT TOO MUCH!!!!!\nConfused as you are about what constitutes as too much\nyou decide to take some gold.\nHow much do you take.\n')
    while True:
        choice = input('>')

        try:
            number = int(choice)
            if number < 50:
                lines()
                print('You hear a voice in the background that says:')
                print('"You are not greedy!!!"')
                print('"Good for you!!!!"')
                print('"Here you\'re free now"')
                print('Something hits your head and falls on the ground')
                print('You look and WOHAAA it\'s a key!')
                print('You use it to unlock yourself and you run for it')
                print('AND YOU ARE FREE!!!!!!')
                lines()
                print('Stupid human, they forgot the gold XD')
                lines()
                exit(1)
            else:
                lines()
                print('"You Greedy bastard" a voice yells')
                print('You deserve to die!!!!')
                dead('A rock falls from the ceiling')

        except ValueError:
            print('See now you\'re just trying to be annoying -_-')
            print('Can you please just give me a number.')
            print('and don\'t spell it out. Just type the stupid number\n')


def back_out():
    '''
    If the player is back here then they deserve to die -_-
    '''
    lines()
    print('You\'re back outside and you see the saw where you left it.\nGiven that you are a chicken and you ran out of the house cause it\'s dark,\nyou see no other choice but to use the saw on your foot')
    dead('You die from the pain')


start()
