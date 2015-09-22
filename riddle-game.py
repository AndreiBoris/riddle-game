from sys import exit
from time import sleep

class Engine(object):

    def __init__(self, a_map):
        self.map = a_map

    def play(self, start_room):
        # this will run for the duration of the game, using self.map to
        # navigate between the rooms

        next_room = self.map.play(start_room)

        while next_room != 'end':
            next_room = self.map.play(next_room)
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
    extra = ""
    helper ="""
Here are some actions that you can take:
- walk (somewhere)
- inventory (or inv)
- look around
- intro
- touch (something)
- take (something)
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
                print self.extra
                print self.bearings
            if action == "intro":
                print self.intro
                print self.bearings
            if action == "inventory" or action == "inv":
                inv.show()
                print "\nWhat do you do? \n"
        print "\nYou attempt to %s." % action
        sleep(0)
        return action

class StartingRoom(Room):

    start_of_game = True
    good_moves = ['go north', 'walk north']
    bad_moves = ['walk south', 'walk east', 'walk west', 'go south', 'go east',
                'go west']
    wake_up = """You wake up.

Your mind is foggy but slowly you get your bearings.

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

    door_open = False
    attempted_door = False
    touched_indentations = False
    good_moves = ['touch door', 'place stones', 'back away', 'go back',
                    'walk south', 'go south', 'take bag', 'open door',
                    'go north', 'walk north', 'touch indentations',
                    'place stone', 'touch indentation']
    bad_moves = ['go east', 'walk east', 'go west', 'walk west']
    stones = {'Stone of Peace': False, 'Stone of Silence': False,
            'Stone of Respect': False, 'Stone of Practice': False,
            'Stone of Friendship': False, 'Stone of Connection': False}
    intro = """
This door is beautiful. It is probably the best door you have ever seen. Picture
the nicest door you ever saw. That's what this looks like. It has three small
indentations on either side of it."""
    extra = """
There is a bag made out of fabric on the floor next to the door. It is seriously
messing up how cool this door looks.

The door looks so beautiful that you would love to touch it, not that you'd
expect to learn anything. There are also some more useful looking indentations
that are within reach."""
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
            print "\nNo door has the right to feel this good."
            sleep(3)
            print "\nReluctantly, you back away."
            sleep(2)
            return self.enter()

        if action == 'touch indentation' or action == 'touch indentations':
            self.touched_indentations = True
            print "\nThese indentations are cold."
            sleep(2)
            have_stone = False
            for stone in self.stones.keys():
                if stone in inv.items:
                    have_stone = True
            sleep(2)
            if have_stone:
                print """
It seems like you could place some of these riddle stones into some of these
indentations."""
                return self.enter()
            else:
                print """
You wonder what these might be for. Perhaps they are meant to hold something?
But what? You'll have to look around."""
                return self.enter()

        if action == 'place stones' or action == 'place stone':
            placed = False
            for stone in self.stones.keys():
                if stone in inv.items:
                    inv.remove(stone)
                    print """
You take The %s out of the bag and place it the indentation where it fits best.""" % stone
                    self.stones[stone] = True
                    placed = True
                    sleep(2.2)
            if placed:
                return self.enter()
            if not placed:
                print """
You pull out a stone and get ready to place it on the wall. Except in your hand
there is nothing at all. It is empty. How silly of you."""
                sleep(4)
                return self.enter()

        if (action == 'go south' or action == 'go back' or
            action == 'back away' or action == 'walk south'):
            return 'middle'

        if action == 'take bag':
            print """
There is something sticky under the bag so you have to really give it a tug
before you can lift it up."""
            sleep(3)
            print """
Upon closer inspection, it doesn't look half bad! Rough, rugged, tough, serious.
The bag reminds you enough of your childhood that you think it's best if you
hold onto it. Might come in handy."""
            inv.add('dirty bag')
            self.bag = False
            self.extra = """
Ah, good! That dirty bag is no longer messing up the look of the sweet, sweet
door. All is well.

The door looks so beautiful that you would love to touch it, not that you'd
expect to learn anything. There are also some more useful looking indentations
that are within reach."""
            sleep(6)
            return self.enter()

        if action == 'open door':
            if self.stone_count() > 3:
                if self.attempted_door:
                    print """
Using your past failure to open the door to your advantage, you waste no time
and pull on the door after turning the handle."""
                    sleep(4)
                    print "\nSuccess!"
                    self.door_open = True
                    return self.enter()
                else:
                    print """
You turn the handle and give the door a good push. Nothing. What? But the
stones! You had hoped that this would be enough?"""
                    sleep(4)
                    print "\nWhat is missing? What needs be done?"
                    sleep(3)
                    print "\nYour mind spins around in despair..."
                    sleep(4)
                    action = "sink into deeper despair"
                    door_count = 0
                    while action != "pull door" and door_count < 6:
                        door_count += 1
                        print "I guess you might as well %s." % action
                        action = raw_input("\nBut would you also like to try to do something else? > ")
                    print "In a desperate effort, you pull on the door handle."
                    sleep(2)
                    print "\nNice."
                    sleep(2)
                    print "\nThe door is now open."
                    self.door_open = True
                    return self.enter()
            else:
                print """
You turn the handle and give the door a good push. Nothing. You give up,
defeated."""
                sleep(4)
                print """
OF COURSE! This door is a 'pull'! You turn the handle and triumphantly pull on
the door!"""
                sleep(5)
                print "\nNope. Definitely not opening. At least you gave it your all!"
                sleep(2.5)
                print "\n(It wasn't enough.)"
                self.attempted_door = True
                sleep (1.5)
                return self.enter()

    def stone_count(self):
        count = 0
        for stone in self.stones.keys():
            if self.stones[stone]:
                count += 1
        return count



class Map(object):

    rooms = {'start': StartingRoom(), 'middle': MiddleRoom(), 'door': TheDoor()}

    def play(self, next_room):
        print "\n" * 35
        return self.rooms[next_room].enter()

the_map = Map()
inv = Inventory()
game = Engine(the_map)
game.play('start')

# TODO: Make the sleep() between turns in the action method 1 second when done
# testing everything
# TODO: Make sure the inventory is clear for the start of the game.
# TODO: make sure the touched_indentations attribute actually helps to give clues
