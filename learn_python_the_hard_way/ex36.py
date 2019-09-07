'''
This script is a simple clone of Zork
It's nothing fancy but it shows how well I grasped the basics of the python language
'''
from sys import exit


def lines():
    '''
    This does nothing but prints lines to make things look pretty (well I think they will look pretty)
    '''
    print('-' * 10)


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
    print('''
You enter a large dark hall.
You look around in the dark using only the light comming from oustide 
and manage to see that there are 2 doors other than the one you came from
The door on your right says 'DO NOT ENTER' 
and the door on your left says 'ENTER IF YOU DARE'
Which door do you choose?\n
            ''')

    while True:
        choice = input('>')

        if 'left' in choice:
            pass
        elif 'right' in choice:
            pass
        elif 'back' in choice:
            back_out()
        else:
            print('This is no time to act stupid, just make up your mind')


def back_out():
    '''
    If the player is back here then they deserve to die -_-
    '''
    lines()
    print('''
You're back outside and you see the saw where you left it.
Given that you are a chicken and you ran out of the house cause it's dark,
you see no other choice but to use the saw on your foot
            ''')
    dead('You die from the pain')


start()
