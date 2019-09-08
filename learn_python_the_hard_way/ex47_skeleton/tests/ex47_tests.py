import nose.tools as nt
from ex47.game import Room


def test_room():
    gold = Room('GoldRoom',
                '''This room has gold in it you can grab. There's a door to the north''')
    nt.assert_equal(gold.name, 'GoldRoom')
    nt.assert_equal(gold.paths, {})


def test_room_paths():
    center = Room('Center', 'Test room in the center')
    north = Room('North', 'Test room in the north ')
    south = Room('South', 'Test room in the south ')

    center.add_path({'north': north, 'south': south})
    nt.assert_equal(center.go('north'), north)
    nt.assert_equal(center.go('south'), south)


def test_map():
    start = Room('Start', 'You can go west and down a hole.')
    west = Room('Trees', 'There are trees, you can go east.')
    down = Room('Dungeon', 'It\'s dark down here, you can go up')

    start.add_path({'west': west, 'down': down})
    west.add_path({'east': start})
    down.add_path({'up': start})

    nt.assert_equal(start.go('west'), west)
    nt.assert_equal(start.go('west').go('east'), start)
    nt.assert_equal(start.go('down').go('up'), start)
