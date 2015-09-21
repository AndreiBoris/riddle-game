from sys import exit
from time import sleep

class Engine(object):

    def __init__(self, a_map):
        self.map = a_map

    def play(self, start_room):
        # this will run for the duration of the game, using self.map to
        # navigate between the rooms

        print "You wake up.\n"
        print "Your mind is foggy but slowly you get your bearings."

        next_room = self.map.play(start_room)

        while next_room != 'end':
            next_room = self.map.play(next_room)
            # intro doesn't automatically play after a room has been visited
            #self.map.rooms[next_room].visited = True
        if next_room == 'end':
            self.map.play(next_room)


class Inventory(object):

    items = []

    def show(self):
        print "\nYour inventory:"
        for item in self.items:
            print item
        if not self.items:
            print "Just the clothes on your back."

    def add(self, new_item):
        self.items.append(new_item)

    def remove(self, old_item):
        self.items.remove(old_item)

class Room(object):

    visited = False
    valid = ['help', 'walk', 'walk north', 'walk south', 'walk east', 'walk west',
            'go', 'go north', 'go south', 'go east', 'go west', 'inventory',
            'inv', 'intro', 'look around', 'take']
    vague_moves = ['walk', 'go', 'take']
    bad_moves = []
    good_moves = []
    helper ="""
Here are some actions that you can take:
- walk (must qualify with a compass direction, i.e. north/south/east/west)
- inventory (or inv)
- look around
- intro
- touch
"""
    bearings = """
There appears to be no way to get your bearings in this generic room.

What do you do?
"""

    def action(self):
        # basic action options for any room
        action = None
        while action not in self.good_moves:
            action = raw_input("> ").lower()
            if action not in self.valid and action not in self.good_moves:
                print "\nI'm sorry, but you can't %r.\n" % action
            if action in self.bad_moves:
                print "\nYou can't go there from here.\n"
            if action in self.vague_moves:
                print "\nCommunication is important. Please be more specific!\n"
            if action == 'help':
                print self.helper
            if action == 'look around':
                print self.bearings
            if action == "intro":
                print self.intro
                print self.bearings
            if action == "inventory" or action == "inv":
                inv.show()
                print "\nWhat do you do? \n"
        print "\nYou %s." % action
        sleep(1)
        print "\n" * 35
        return action

class StartingRoom(Room):

    start_of_game = True
    good_moves = ['go north', 'walk north']
    bad_moves = ['walk south', 'walk east', 'walk west', 'go south', 'go east',
                'go west']
    wake_up = """
You are in a blue-tinted room surrounded by what seems to be drywall. You are
lying on a mattress sprawled in the middle of the room. You're dressed normally.
Nothing seems to have gone wrong but you don't have a clear idea of where you
are or why."""
    intro = """
This is the room you woke up in. Apart from the spartan set up and the random
mattress placement, it's not so bad."""
    bearings = """
There is a hallway to the north.

What do you do?\n"""

    def enter(self):
        if self.start_of_game == True:
            print self.wake_up
            self.start_of_game = False
        print self.bearings
        action = self.action()
        if action == "go north" or action == "walk north":
            return "middle"

class MiddleRoom(Room):

    good_moves = ['go east', 'walk east', 'walk south', 'walk east',
                    'walk west', 'go south', 'go east', 'go west', 'go north',
                    'walk north']
    bad_moves = []
    intro = """
This room is huge - remarkably so. It makes one wonder what kind of building was
designed to hold such a mammoth. Despite its awe-inspiring size, the upkeep
leaves much to be desired. It dripping with old newspapers that have been left
lying around and in various makeshift beddings. Dripping because the ceiling is
soaked - evidently the roof doesn't do such a great job keeping the rain out."""
    bearings = """
To the north there is a door that is in incongruously good condition. To the
east is some sort of office wing. To the west there is a dark tunnel. To the
south is a short hallway leading to a small apartment room.

What do you do?\n"""
    def enter(self):
        if self.visited == False:
            print self.intro
        self.visited = True
        print self.bearings
        action = self.action()
        if action == "go south" or action == "walk south":
            return "start"
        if action == "go east" or action == "walk east":
            return "right"
        if action == "go west" or action == "walk west":
            return "left"
        if action == "go north" or action == "walk north":
            return "door"

class TheDoor(Room):

    good_moves = ['touch door', 'place stones', 'back away', 'go back',
                    'walk south', 'go south', 'take bag', 'open door',
                    'go north', 'walk north', 'touch indentations']
    bad_moves = ['go east', 'walk east', 'go west', 'walk west']
    stones = {'stone of peace': False, 'stone of silence': False,
            'stone of respect': False, 'stone of practice': False,
            'stone of friendship': False, 'stone of connection': False}
    intro = """
This door is beautiful. It is probably the best door you have ever seen. Picture
the nicest door you ever saw. That's what this looks like. It has three small
indentations on either side of it."""
    bearings = """
You are in front of the immaculate door. Behind you, to the south, is the big,
dripping room.

What do you do?\n"""

    def enter(self):
        if self.visited == False:
            print self.intro
        self.visited = True
        print self.bearings
        action = self.action()
        if action == 'touch door':
            print "A door has no right to feel this good."
            return self.enter()
        if action == 'place stones':
            for stone in self.stones.keys():
                if stone in inv.items:
                    pass
        if (action == 'go south' or action == 'go back' or
            action == 'back away' or action == 'walk south'):
            return 'middle'


class Map(object):

    rooms = {'start': StartingRoom(), 'middle': MiddleRoom(), 'door': TheDoor()}

    def play(self, next_room):
        return self.rooms[next_room].enter()

the_map = Map()
inv = Inventory()
game = Engine(the_map)
game.play('start')


# TODO: if returning to starting room, there shouldn't be the wake-up intro
# message
# TODO: change messages after the first time being in the room, though this
# information should be accessible using some kind of function.
# TODO: Opening mattress bit has to be just for the first instance of the room,
# it shouldn't even be accessible with intro
