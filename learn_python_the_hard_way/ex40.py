class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(['Happy birthday to you',
                   'I don\'t want to get sued', 'so I\'ll stop right here'])

bulls_on_parade = Song(['They rally around tha family',
                        'With pocketd full of shells'])

happy_bday.sing_me_a_song()
print('\n')
bulls_on_parade.sing_me_a_song()
