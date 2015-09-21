class Engine(object):

    def __init__(self, a_map):
        self.map = a_map

class Inventory(object):

    keys = []

    def show(self):
        print "\nYour inventory:"
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
            'inv', 'bearings', 'restart']
    vague_moves = ['walk', 'go']
    bad_moves = []
    good_moves = []
    helper ="""
Here are some actions that you can take:
- walk (must qualify with a compass direction, i.e. north/south/east/west)
- inventory (or inv)
- bearings
- restart (the room)
"""
    bearings = """
There appears to be no way to get your bearings in this generic room.

What do you do?
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

    def action(self):
        # basic action options for any room
        action = None
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
            if action == 'bearings':
                print self.bearings
            if action == "restart":
                print self.intro
                print self.bearings
            if action == "inventory" or action == "inv":
                inv.show()
                print "\nWhat do you do? \n"
        print "\nYou %s." % action

class StartingRoom(Room):

    good_moves = ['go north', 'walk north']
    bad_moves = ['walk south', 'walk east', 'walk west', 'go south', 'go east',
                'go west']
    intro = """You wake up.
Your mind is foggy but slowly you get your bearings. You are in a blue-tinted
room surrounded by what seems to be drywall. You are lying on a mattress
sprawled in the middle of the room. You're dressed normally. Nothing seems to
have gone wrong but you don't have a clear idea of where you are or why."""
    bearings = """
There is a hallway to the north.

What do you do?\n"""

    def enter(self):
        print self.intro
        print self.bearings
        action = self.action()
        if action == "go north" or action == "walk north":
            return "middle"

class MiddleRoom(Room):

    good_moves = ['go east', 'walk east', 'walk south', 'walk east',
                    'walk west', 'go south', 'go east', 'go west']
    bad_moves = []
    intro = """This room is huge - remarkably so. It makes one wonder what kind
of building was designed to hold such a mammoth. Despite its awe-inspiring size,
the upkeep leaves much to be desired. It dripping with old newspapers that have
been left lying around and in various makeshift beddings. Dripping because the
ceiling soaked - evidently the roof doesn't do such a great job keeping the rain
out."""
    bearings = """
To the north there is a door that is in incongruously good condition. To the
east is some sort of office wing. To the west there is a dark tunnel. To the
south is a short hallway leading to a small apartment room.

What do you do?\n"""
    def enter(self):
        print self.intro
        print self.bearings
        action = self.action()
        if action == "go south" or action == "walk south":
            return "start"
        if action == "go east" or action == "walk east":
            return "right"
        if action == "go west" or action == "walk west":
            return "left"


class Map(object):

    rooms = {'start': StartingRoom(), 'middle': MiddleRoom()}

the_map = Map()
game = Engine(the_map)
inv = Inventory()
start = StartingRoom()
start.enter()

# TODO: if returning to starting room, there shouldn't be the wake-up intro
# message
# TODO: change messages after the first time being in the room, though this
# information should be accessible using some kind of function.
