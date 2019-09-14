import nose.tools as nt
import gothonweb.planisphere as game


def test_room():
    gold = game.Room('GoldRoom', 'This room has gold in it')

    nt.assert_equal(gold.name, 'GoldRoom')
    nt.assert_equal(gold.path, {})


def test_room_path():
    center = game.Room('Center', 'Test room center')
    north = game.Room('North', 'Test room north')
    south = game.Room('South', 'Test room south')

    center.add_paths({'north': north, 'south': south})
    nt.assert_equal(center.go('north'), north)
    nt.assert_equal(center.go('south'), south)


def test_map():
    start = game.Room('Start', 'You can go west and down a hole')
    west = game.Room('Trees', 'There are trees here, you can go east')
    down = game.Room('Dungeon', 'It\'s dark down here, you can go up')

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    nt.assert_equal(start.go('west'), west)
    nt.assert_equal(start.go('west').go('east'), start)
    nt.assert_equal(start.go('down').go('up'), start)


def test_gothon_game_map():
    start_room = game.load_room(game.START)
    nt.assert_equal(start_room.go('shoot!'), game.generic_death)
    nt.assert_equal(start_room.go('dodge!'), game.generic_death)

    room = start_room.go('tell a joke')
    nt.assert_equal(room, game.laser_weapon_armory)
