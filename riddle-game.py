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

    valid = ['help', 'walk', 'walk north', 'walk south', 'walk east', 'walk west',
            'go', 'go north', 'go south', 'go east', 'go west', 'inventory',
            'inv']
    vague_moves = ['walk', 'go']
    helper ="""
Here are some actions that you can take:
- walk
(must qualify with a compass direction, i.e. north/south/east/west)
-inventory
"""

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

    good_moves = ['go north', 'walk north']
    bad_moves = ['walk south', 'walk east', 'walk west', 'go south', 'go east',
                'go west']

    def enter(self):
        print "You wake up. \n"
        print "Your mind is foggy but slowly you get your bearings."
        print "You are in a blue-tinted room surrounded by what seems to be"
        print "drywall. You are lying on a mattress sprawled in the middle of"
        print "the room. You're dressed normally. Nothing seems to have gone"
        print "wrong but you don't have a clear idea of where you are or why. \n"
        print "There is a hallway to the north. \n"
        print "What do you do? (type 'help' for valid actions)\n"
        action = 'invalid'
        while action not in self.good_moves:
            action = raw_input("> ").lower()
            if action not in self.valid:
                print "\nI don't understand %r. Type 'help' if you are lost.\n" % action
            if action in self.bad_moves:
                print "\nYou can't go there from here.\n"
            if action in self.vague_moves:
                print "\nWhere would you like to %s?\n" % action
            if action == 'help':
                print self.helper
        print "OK, let's %s!" % action



class Map(object):
    pass

the_map = Map()
game = Engine(the_map)
inv = Inventory()
start = StartingRoom()
start.enter()
