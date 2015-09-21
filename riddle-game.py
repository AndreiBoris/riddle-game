class Engine(object):

    def __init__(self, a_map):
        self.map = a_map

class Inventory(object):

    keys = ["key to sorrow", "key to gratitude"]

    def show(self):
        print "Your inventory:"
        for key in self.keys:
            print key
        if not self.keys:
            print "Just the clothes on your back."

    def add(self, new_key):
        self.keys.append(new_key)

    def clear(self):
        del self.keys[:]

class Room(object):

    valid = ['help', '']

    def inventory(self):
        # somehow access inventory
        pass

    def move(self):
        # move in various directions using Map
        pass

    def help(self):
        # basic instructions of what the player can do are printed
        pass

class StartingRoom(Room):

    def enter(self):
        print "You wake up. \n"
        print "Your mind is foggy but slowly you get your bearings."
        print "You are in a blue-tinted room surrounded by what seems to be"
        print "drywall. You are lying on a mattress sprawled in the middle of"
        print "the room. You're dressed normally. Nothing seems to have gone"
        print "wrong but you don't have a clear idea of where you are or why. \n"
        print "What do you do?\n"
        action = raw_input("> ").lower()
        print action


class Map(object):
    pass

the_map = Map()
game = Engine(the_map)
inv = Inventory()
start = StartingRoom()
start.enter()
