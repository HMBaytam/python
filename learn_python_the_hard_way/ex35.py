from sys import exit


def gold_room():
    print('This room is full of gold. How much do you take?')

    choice = input('>')
    # the code below is a fix to the bug found in the code at the bottom of this block
    try:
        how_much = int(choice)
        if how_much < 50:
            print('Nice, you\'re not greedy!\n')
            final()
        else:
            dead('You greedy bastard!')
    except ValueError:
        dead('Man, learn to type a number')

    # the code below has a bug that needed a fix
    # if '0' in choice or '1' in choice:
    #     how_much = int(choice)
    # else:
    #     dead('Man, learn to type a number')


def bear_room():
    print('There is a bear here.')
    print('The bear has a bunch of honey.')
    print('The fat bear is in front of another door.')
    print('How are you going to move the bear?')
    bear_moved = False

    while True:
        choice = input('>')

        if choice == 'Take honey':
            dead('The bear looks at you then slaps your face off.')
        elif choice == 'taunt bear' and not bear_moved:
            print('The bear has moved from the door.')
            print('You can go through it now.')
            bear_moved = True
        elif choice == 'taunt bear' and bear_moved:
            dead('The bear gets pissed off and chews your leg off.')
        elif choice == 'open door' and bear_moved:
            gold_room()
        else:
            print('I got no idea what that means.')


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


def dead(why):
    print(why, 'Good job!')
    exit(0)


def start():
    print('You are in a dark room.')
    print('There is a door to your right and left.')
    print('Which one do you take?')

    choice = input('>')

    if choice == 'left':
        bear_room()
    elif choice == 'right':
        cthulhu_room()
    else:
        dead('You stumble around the room until you starve.')

# The code block below is an new feature I wrote that is not in the book


def final():
    print('You pick up your loot and look up to find three doors')
    print('A door up in front of you, a door to your right, and a door to your left')
    print('Which one do you choose?')

    choice = input('>')

    if 'left' in choice:
        cthulhu_room()
    elif 'right' in choice:
        dead('You open the door and trip on a wire\n the door slams shut and the walls start closing in with no exit in sight\n')
    else:
        print('Awesome! You are now outside the building with your loot!\nYou have won the game!')
        exit(0)


start()
