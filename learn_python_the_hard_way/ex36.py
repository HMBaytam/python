'''
This script is a simple clone of Zork
It's nothing fancy but it shows how well I grasped the basics of the python language
'''
from sys import exit


def start():
    '''
    The game starts from this scene. pretty simple
    '''
    print('You wake up to find yourself in front of an old house.')
    print('You\'re leg is tied to a chian that leads inside the house.')
    print('You find a saw next to you.')
    print('Do you follow the chain or saw your foot off?\n')

    while True:
        choice = input('>')

        if 'follow' in choice:
            main_hall()
        elif 'saw' in choice:
            dead('You die from the pain.')
        else:
            print('That makes no sense\n')


def dead(sentence):
    '''
    This is the death scene
    '''
    print(sentence, ' Good job!\n')
    exit(0)


def main_hall():
    '''
    The first room the player sees when they enter the house
    '''
    print('You ')


start()
