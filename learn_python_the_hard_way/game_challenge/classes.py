from sys import exit


class Main(object):
    def __init__(self):
        print('Hello and welcome to the world of nothing!\n')
        print('Follow the instructions in each section of the game.')
        print('If you don\'t you might find yourself in a situation that you really want to avoid!\n')
        Start.beginning(self)

    def dead(self, sentence):
        print(sentence, ' Good job!')
        exit(0)


class Start(object):
    def beginning(self):
        print('-' * 75)
        print('You wake up and find yourself lying on the drive way of an abandoned house')
        print('The front door of the house is slightly cracked')
        print('You also see a mailbox that has a letter in it')

        while True:
            self.action = input('>>')

            if 'mail' in self.action or 'letter' in self.action:
                print('\nthe letter is empty for now')
                exit(0)
            elif 'front' in self.action:
                MainHall.enter(self)
            else:
                print('What are you saying?')


class MainHall(object):
    def enter(self):
        print('You enter a large dark hall.\nYou look around in the dark using only the light comming from oustide\nand manage to see that there are 3 doors other than the one you came from\nThe door on your right says \'DO NOT ENTER\'\nand the door on your left says \'ENTER IF YOU DARE\'\nand a door right in front of you that has no sign\nYou also see that the chain around your foot is tied to the ground here\nbut you can\'t seem to figure out how to unlock the chain from your foot\nWhich door do you choose?\n')

        while True:
            self.action = input('>>')

            if 'left' in self.action:
                BearRoom.enter(self)
            elif 'right' in self.action:
                CthulhuRoom.enter(self)
            elif 'front' in self.action:
                WolfRoom.enter(self)
            elif 'out' in self.action:
                Main.dead(self, 'The door closes on your face')
            else:
                print('\n')
                print('This is no time to act stupid, just make up your mind')
                print('\n')


class GoldRoom(object):
    def enter(self):
        print('You enter a room full of gold!\nWith a sign on top that says take as much as you want,\nBUT NOT TOO MUCH!!!!!\nConfused as you are about what constitutes as too much\nyou decide to take some gold.\nHow much do you take.\n')

        while True:
            self.choice = input('>>')

            try:
                number = int(self.choice)
                if number < 50:
                    print('You hear a voice in the background that says:')
                    print('"You are not greedy!!!"')
                    print('"Good for you!!!!"')
                    print('"Here you\'re free now"')
                    print('Something hits your head and falls on the ground')
                    print('You look and WOHAAA it\'s a key!')
                    print('You use it to unlock yourself and you run for it')
                    print('AND YOU ARE FREE!!!!!!')
                    print('Stupid human, they forgot the gold XD')
                    exit(1)
                else:
                    print('"You Greedy bastard" a voice yells')
                    print('You deserve to die!!!!')
                    Main.dead(self, 'A rock falls from the ceiling')
                    exit(0)

            except ValueError:
                print('See now you\'re just trying to be annoying -_-')
                print('Can you please just give me a number.')
                print('and don\'t spell it out. Just type the stupid number\n')


class CthulhuRoom(object):
    def enter(self):
        print('Here you see the great evil Cthulhu.')
        print('He, it, whatever stares at you and you go insane.')
        print('Do you flee for your life or eat your head?')

        while True:
            self.choice = input('>')

            if 'flee' in self.choice or 'run' in self.choice:
                MainHall.enter(self)
            elif 'head' in self.choice:
                Main.dead(self, 'Well that was tasty!')
            else:
                print('Stop wasting time!!\n')


class BearRoom(object):
    def enter(self):
        print('There is a bear here.')
        print('The bear has a bunch of honey.')
        print('The fat bear is in front of another door.')
        print('How are you going to move the bear?')
        self.bear_moved = False

        while True:
            self.choice = input('>')

            if self.choice == 'Take honey':
                Main.dead(
                    self, 'The bear looks at you then slaps your face off.')
            elif self.choice == 'taunt bear' and not self.bear_moved:
                print('The bear has moved from the door.')
                print('You can go through it now.')
                self.bear_moved = True
            elif self.choice == 'taunt bear' and self.bear_moved:
                Main.dead(
                    self, 'The bear gets pissed off and chews your leg off.')
            elif self.choice == 'open door' and self.bear_moved:
                GoldRoom.enter(self)
            else:
                print('I got no idea what that means.')


class WolfRoom(object):
    def enter(self):
        print('Oh uh! A rabid wold walks in and blocks the exit door')
        print('You can see that the wolf wants to eat your head off')
        print('There is a 2x4 on the floor next to you (how lucky)')

        self.wolf_health = 100
        self.weapon = False
        while True:

            if self.wolf_health > 0:
                print(f'\nThe wolf has {str(self.wolf_health)} HP\n')
            else:
                print('\nThe wold is dead\n')
            self.action = input('>>')

            if 'grab' in self.action or '2x4' in self.action:
                self.weapon = True
                print('\nYou are now holding the 2x4, now what?\n')
            elif 'hit' in self.action and not self.weapon:
                print('\nWith what? the 2x4 you\'re not carrying?\n')
            elif 'hit' in self.action and self.weapon and self.wolf_health > 0:
                self.wolf_health -= 50
                if self.wolf_health > 0:
                    print('\nThe wolf is badly injured')
                else:
                    print('\nYOU KILLED THE WOLF!!')
            elif 'hit' in self.action and self.weapon and self.wolf_health == 0:
                print('\nYou already killed the wolf')
            elif 'door' in self.action and self.wolf_health == 0:
                GoldRoom.enter(self)
            elif 'door' in self.action and self.wolf_health > 0:
                print(
                    '\nThe wolf starts growling to remind you, THAT IT\'s STILL THERE\n')
            else:
                print('\nDo you really think this is the time to screw around?\n')
