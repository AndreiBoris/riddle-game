from time import sleep
from random import randint
from random import choice
from sys import exit
import pickle

# all_strings is just what is sounds like: anything that is imported from it
# is a string or a function that is a combination of strings, time.sleep() and
# raw_input prompts that are just meant to control the flow of readable content

import all_strings

# The general breakdown of what this game does is as follows:
#
# Each of the room classes are instantiated. These room classes are
# StartingRoom, MiddleRoom, TheDoor, Left, Right, End, World, Racetrack,
# Alone, Butcher, DiningRoom and Battlefield. Classes Inventory and Map are then
# also instantiated. If there is a saved.py file in the folder (a file that
# this game makes when the player make a 'save' action) then a custom instance
# of SavedGame is unpickled from that saved.py file, otherwise a default version
# of SavedGame is instantiated. The Loader is then instantiated with this
# SavedGame object as an argument and Engine is instantiated with the Loader
# and Map objects as arguments.
#
# The Game object then prompts the player to start a New game or to Load the
# saved game. A new game just runs the default values as seen below, the load
# option would use the Loader's load_it() method to extract state attributes
# from the SavedGame object it had passed into it and alter all the room
# objects in order to change the current state of the game by changing a number of
# significant attributes that they have like stone_available, visited, etc.
# load_it() returns a starting position and this is then fed into a while loop
# in Engine's play() method that keeps running Map's play() method which the
# enter() methods of the various room objects (each of which return a string
# that can be fed into the Map.play() method to get a new room).
#
# It might be significant to note that the rooms that are refered to as
# riddle rooms are Alone, Battlefield, Butcher, DiningRoom, World, and
# Racetrack. These are special in that they have the stone_here attributes
# as set to true and the player has to solve riddles in them in order to get a
# stone from each one in order to collect at least 4 stones and then place them
# in indentations inside the TheDoor in order to get into the End room.


class Engine(object):

    def __init__(self, a_map, loader):
        self.map = a_map

# The loader carries a set of saved-game properties and can be called upon by
# Engine to apply to properties to the current file.

        self.loader = loader

    def play(self):
        # this will run for the duration of the game, using self.map to
        # navigate between the rooms

        print all_strings.start_game
        choice = ''
        while choice != 'new' and choice != 'load':
            choice = raw_input('\n\n\n> ').lower()
        if choice == 'new':
            first_room = 'start'
        elif choice == 'load':

# If there is is no saved file, the loader has default properties loaded to it
# and will act just like a running a new game. load_it() changes the state of
# the room objects defined lower down in this file and returns only the starting
# room (i.e. where the save was made.)

            first_room = self.loader.load_it()

# the play() method in the Map() class runs the enter() method of the room
# objects. The room objects return markers that can be put into this play().

        next_room = self.map.play(first_room)

        while next_room != 'end':
            next_room = self.map.play(next_room)
        if next_room == 'end':
            self.map.play(next_room)


class Inventory(object):

    items = []

# 3 failed riddles mean the game cannot be completed, so at that point it fails.

    failed_riddles = 0

    def show(self):
        print '\nYour inventory:'
        for item in self.items:
            print item
        if not self.items:
            print all_strings.empty_inv

    def add(self, new_item):
        self.items.append(new_item)

# This is for an aethetic reason - one item 'dirty bag' fits better at the top
# of the inventory, so this method is called.

    def add_to_top(self, new_item):
        self.items.insert(0, new_item)

    def remove(self, old_item):
        self.items.remove(old_item)

# The player cannot carry more than 1 stone without a bag.

    def stones_carried(self):
        count = 0
        for item in self.items:
            if item.split()[0] == 'Stone':
                count += 1
        return count

# Gives warning messages and finally a terminating one.

    def end_if_failed(self):
        if self.failed_riddles == 1:
            print all_strings.lost_1
        if self.failed_riddles == 2:
            print all_strings.lost_2
        if self.failed_riddles >= 3:
            print all_strings.lose_game
            exit(1)


class Room(object):

# Some of these are not used for some of the rooms.

    name = ''
    current_room = False
    guesses_left = 5
    solved = False
    stone_here = False
    visited = False
    bad_moves = []
    good_moves = []
    extra = ''
    helper = all_strings.helper
    bearings = ''
    attempted = False
    attempt_moves = []
    stone_moves = ['take stone', 'pick up stone', 'grab stone']
    bearings_final = ''
    extra_final = ''
    room_stone = ''
    room_stone_message = ''

    def action(self):
        # basic action options for any room
        action = raw_input("> ").lower().strip()

# Each room has a specific mutable set of actions that are good_moves, if one
# of those is picked, that action is returned and fed into the room's script,
# otherwise this action() method handles it and then reprompts the player to
# make another action.

        while action not in self.good_moves:

# Having the 'touch stone' line here saves having to put it into each
# individual room.

            if action == 'touch stone' and 'take stone' in self.good_moves:
                print all_strings.touch_stone

# Saver() relies on taking all the room objects that are initialized at the
# bottom of this code.

            elif action == 'save':
                confirm = raw_input('\nAre you sure you want to save? y/n > ').lower()
                if confirm == 'y' or confirm == 'yes':
                    the_saver = Saver(start_room, middle_room, door_room, left_room,
                                        right_room, battlefield_room, dining_room,
                                        butcher_room, alone_room, racetrack_room,
                                        world_room, inv, self.name)

# the save() method returns a SavedGame() object that has had the attributes
# of the current room objects loaded into it.

                    saved_file = the_saver.save()
                    with open('saved.py', 'wb') as save_doc:
                        pickle.dump(saved_file, save_doc, pickle.HIGHEST_PROTOCOL)
                    print '\nGame saved.'
                    print all_strings.action_prompt
                else:
                    print all_strings.action_prompt

            elif action == 'quit' or action == 'exit':
                confirm = raw_input('\nAre you sure you want to quit? y/n > ').lower()
                if confirm == 'y' or confirm == 'yes':
                    print all_strings.goodbye
                    exit(1)
                else:
                    print all_strings.action_prompt

            elif action in self.bad_moves:
                print all_strings.bad_moves

            elif action == "take":
                print all_strings.action_take

            elif action == "talk":
                print "\n%s\n" % choice(all_strings.talking)

            elif action == "go":
                print all_strings.action_go

            elif action == "walk":
                print all_strings.action_walk

            elif action == "touch":
                print all_strings.action_touch

            elif action == "sleep":
                print all_strings.action_sleep

            elif action == 'help':
                print all_strings.line_break
                print "\n" * 6
                print self.helper

            elif action == 'look around' or action == 'look':
                print all_strings.line_break
                print "\n" * 8
                print self.extra
                print self.bearings

            elif action == "intro":
                print all_strings.line_break
                print "\n" * 6
                print self.intro
                print self.bearings

            elif action == "inventory" or action == "inv":
                print all_strings.line_break
                print "\n" * 4
                inv.show()
                print all_strings.action_prompt

            elif action == "sit" or action == "sit down":
                print all_strings.action_sit

            elif action == "stand":
                print all_strings.action_stand

            elif action == "wait":
                print all_strings.action_wait

            elif action == "lie down":
                print all_strings.action_lie

            else:
                print "\nI'm sorry, but you can't %r.\n" % action

            action = raw_input("> ").lower().strip()

# This only plays when one of the good_moves is chosen.

        print "\nYou attempt to %s." % action
        sleep(0.75)
        return action

    def stone_available(self):

# This runs at the beginning of each riddle room (except for Alone(), see
# specific comments for that one) and gives the player the option to pick up
# the stone that is yielded at the end of any riddle.

        if (self.stone_here and self.solved and
        self.stone_moves[0] not in self.good_moves):
            for option in self.stone_moves:
                self.good_moves.append(option)
        if not self.stone_here and self.stone_moves[0] in self.good_moves:
            for option in self.stone_moves:
                self.good_moves.remove(option)

# correct_intro() Decides which messages to play when enter() is run in any
# room.

    def correct_intro(self):
        if self.visited == False:
            print self.intro
        self.visited = True

        if not self.current_room:
            print self.bearings

        elif self.current_room:
            print "\nWhat do you do?\n"

        self.current_room = True

# This method makes sure that once a riddle has been attempted in any given
# riddle room, the actions that allow the player to attempt the riddle get
# disabled.

    def one_attempt_only(self):
        if self.attempted and self.attempt_moves[0] in self.good_moves:
            for option in self.attempt_moves:
                self.good_moves.remove(option)

    def stone_pickup(self):
# If the player does not have the 'dirty bag' then they can only carry one of
# the stones at any given time. NOTE that this means this won't work without
# inv instantiated.

        if inv.stones_carried() >= 1 and "dirty bag" not in inv.items:
            all_strings.no_bag()
            return self.enter()

        if inv.stones_carried() == 0 or "dirty bag" in inv.items:
            self.stone_here = False
            inv.items.append(self.room_stone)
            print self.room_stone_message
            all_strings.enter_to_continue()

# The player gets a hint about what to do with a stone if a certain action was
# performed in door_room. NOTE that this means this won't work without the
# door_room instantiated.

        if door_room.touched_indentations:
            all_strings.indentation_hint()

        self.extra = self.extra_final
        self.bearings = self.bearings_final
        return self.enter()


class StartingRoom(Room):

# The name attributes are important in that they are what is passed into the
# Saver for it to know what the current room is.

    name = 'start'
    start_of_game = True
    pen = True
    good_moves = ['go north', 'walk north', 'take pen', 'touch pen',
                    'take mattress', 'touch mattress', 'lie down', 'sleep',
                    'take junk', 'touch junk', 'pick up pen', 'grab pen']
    bad_moves = ['walk south', 'walk east', 'walk west', 'go south', 'go east',
                'go west']
    pen_moves = ['touch pen', 'take pen', 'grab pen', 'pick up pen']
    wake_up = all_strings.starting_room_wake_up
    extra = all_strings.starting_room_extra1
    intro = all_strings.starting_room_intro
    bearings = all_strings.starting_room_bearings1

    def enter(self):

# Checks good_moves first to avoid errors when trying to remove the options,
# if 'take pen' is there so is 'touch pen' since this is the only spot where
# they get removed. This applied to all similar code at the top of other rooms

        if not self.pen and self.pen_moves[0] in self.good_moves:
            for option in self.pen_moves:
                self.good_moves.remove(option)

        if self.start_of_game == True:
            print self.wake_up
            self.start_of_game = False
            self.visited = True

# corrent_intro means that self.intro only runs automatically the first time a
# room is entered and that self.bearings are only run when the player comes from a
# different room and not when a recursive call is made.

        self.correct_intro()

        action = self.action()

# Non-recursive returns feed back into the_map.play() where it finds the room
# that is being pointed to and runs its enter() method

        if action == "go north" or action == "walk north":
            self.current_room = False
            return "middle"

# Recursive calls are just 'dead end' actions

        if action == "lie down" or action == "sleep":
            all_strings.starting_room_lie()
            return self.enter()

        if action == "touch pen":
            all_strings.starting_room_touch_pen()
            return self.enter()

        if action == "touch mattress":
            all_strings.starting_room_touch_mattress()
            return self.enter()

        if action == "take mattress":
            all_strings.starting_room_take_mattress()
            return self.enter()

        if action == "take junk":
            all_strings.starting_room_take_junk()
            return self.enter()

        if action == "touch junk":
            all_strings.starting_room_touch_junk()
            return self.enter()

        if action in self.pen_moves and action != 'touch pen':
            all_strings.starting_room_take_pen()
            self.pen = False
            inv.items.append("ballpoint pen")
            self.extra = all_strings.starting_room_extra2
            return self.enter()


class MiddleRoom(Room):

    name = 'middle'
    good_moves = ['go east', 'walk east', 'walk south', 'walk east',
                    'walk west', 'go south', 'go east', 'go west', 'go north',
                    'walk north', 'touch newspapers', 'touch newspaper',
                    'take newspaper', 'take newspapers', 'touch rubber',
                    'take rubber', 'take hair', 'touch hair']
    bad_moves = []
    intro = all_strings.middle_room_intro
    extra = all_strings.middle_room_extra
    bearings = all_strings.middle_room_bearings
    def enter(self):

        self.correct_intro()

        action = self.action()

        if action == "go south" or action == "walk south":
            self.current_room = False
            return "start"

        if action == "go east" or action == "walk east":
            self.current_room = False
            return "right"

        if action == "go west" or action == "walk west":
            self.current_room = False
            return "left"

        if action == "go north" or action == "walk north":
            self.current_room = False
            return "door"

        if action == "take hair":
            all_strings.middle_room_take_hair()
            return self.enter()

        if action == "touch hair":
            all_strings.middle_room_touch_hair()
            return self.enter()

        if action == "touch newspapers" or action == "touch newspaper":
            all_strings.middle_room_touch_newspaper()
            return self.enter()

        if action == "take newspapers" or action == "take newspaper":
            all_strings.middle_room_take_newspaper()
            return self.enter()

        if action == "touch rubber":
            all_strings.middle_room_touch_rubber()
            return self.enter()

        if action == "take rubber":
            all_strings.middle_room_take_rubber()
            return self.enter()


class TheDoor(Room):

    name = 'door'
    door_open = False
    attempted_door = False
    touched_indentations = False
    bag_here = True
    good_moves = ['touch door', 'place stones', 'back away', 'go back',
                    'walk south', 'go south', 'take bag', 'open door',
                    'go north', 'walk north', 'touch indentations',
                    'place stone', 'touch indentation', 'take indentations',
                    'take indentation', 'look at indentations',
                    'look at indentation', 'inspect indentations',
                    'inspect indentation', 'touch bag', 'pick up bag',
                    'grab bag']
    bag_moves = ['touch bag', 'take bag', 'pick up bag', 'grab bag']
    bad_moves = ['go east', 'walk east', 'go west', 'walk west']
    stones = {'Stone of Peace': False, 'Stone of Silence': False,
            'Stone of Respect': False, 'Stone of Practice': False,
            'Stone of Friendship': False, 'Stone of Compassion': False}
    intro = all_strings.the_door_intro
    extra = all_strings.the_door_extra1
    bearings = all_strings.the_door_bearings1

    def enter(self):

        self.correct_intro()

        action = self.action()

        if (action == 'go south' or action == 'go back' or
            action == 'back away' or action == 'walk south'):
            self.current_room = False
            return 'middle'

# Can only go north if the door is open.

        if action == 'go north' or action == 'walk north':
            if self.door_open:
                self.current_room = False
                return 'end'
            else:
                all_strings.the_door_believe()
                return self.enter()

        if action == 'touch door':
            all_strings.the_door_touch_door()
            return self.enter()

        if action == "take indentation" or action == "take indentations":
            all_strings.the_door_take_indentations()
            return self.enter()

        if (action == 'touch indentation' or action == 'touch indentations' or
            action == 'look at indentations' or
            action == 'look at indentation' or
            action == 'inspect indentations' or
            action == 'inspect indentation'):
            if action == 'touch indentation' or action == 'touch indentations':
                all_strings.the_door_touch_indentations()
            if action == 'look at indentation' or action == 'look at indentations':
                all_strings.the_door_see_indentations()

# A hint will now be given whenever a stone picked up, pointing the player back
# to these indentations

            self.touched_indentations = True

            have_stone = False
            had_stone = False

            for stone in self.stones.keys():

                if stone in inv.items:
                    have_stone = True
                if self.stones[stone]:
                    had_stone = True

            if have_stone:
                all_strings.the_door_have_stone()
                return self.enter()

            elif had_stone:
                if self.stones['Stone of Peace']:
                    all_strings.the_door_s_peace()
                if self.stones['Stone of Silence']:
                    all_strings.the_door_s_silence()
                if self.stones['Stone of Compassion']:
                    all_strings.the_door_s_compassion()
                if self.stones['Stone of Friendship']:
                    all_strings.the_door_s_friendship()
                if self.stones['Stone of Respect']:
                    all_strings.the_door_s_respect()
                if self.stones['Stone of Practice']:
                    all_strings.the_door_s_practice()
                all_strings.the_door_had_stone()
                return self.enter()

            else:
                all_strings.the_door_no_stone()
                return self.enter()

        if action == 'place stones' or action == 'place stone':
            placed = False

# Try to place a stone into the indentations.

            for stone in self.stones.keys():
                if stone in inv.items:
                    inv.remove(stone)
                    print """
You take The %s and place it the indentation where it fits
best.""" % stone
                    self.stones[stone] = True
                    placed = True
                    all_strings.enter_to_continue()

            if placed:
                return self.enter()

# If the player had no stone, insult the player.

            if not placed:
                all_strings.the_door_not_placed()
                return self.enter()

        if action == 'touch bag':
            all_strings.the_door_touch_bag()
            return self.enter()

        if action in self.bag_moves and action != self.bag_moves[0]:

            if self.bag_here:
                all_strings.the_door_take_bag()
                inv.add_to_top('dirty bag')
                self.bag_here = False
                self.extra = all_strings.the_door_extra2
                return self.enter()

            else:
                print all_strings.the_door_bag
                return self.enter()

        if action == 'open door':

            if self.door_open:
                print all_strings.the_door_already_open
                return self.enter()

# The door will open if there are 4 or more stones placed in the indentations.

            if self.stone_count() > 3:

# If the player had previously tried to open the door, it will be easier this
# time.

                if self.attempted_door:
                    all_strings.the_door_experienced()
                    self.door_open = True
                    self.bearings = all_strings.the_door_bearings2
                    return self.enter()

# If this is the first time that the player tries to open the door, it will be
# harder.

                else:
                    all_strings.the_door_cant_push()
                    action = all_strings.the_door_action
                    door_count = 0
                    while (action != 'pull door' and action != 'pull' and
                            action != 'pull the door' and
                            action != 'pull on door' and
                            door_count < 4):
                        door_count += 1
                        print "\nI guess you might as well %s." % action
                        action = raw_input("\nBut would you also like to try " +
                        "to do something else? > ").lower().strip()
                    all_strings.the_door_can_pull()
                    self.door_open = True
                    self.bearings = all_strings.the_door_bearings2
                    return self.enter()

# If there aren't enough stones in the indentations, the player will fail to
# open the door.

            else:
                all_strings.the_door_struggles()
                self.attempted_door = True
                return self.enter()

# stone_count() is used to determine if the door can open.

    def stone_count(self):
        count = 0
        for stone in self.stones.keys():
            if self.stones[stone]:
                count += 1
        return count


class Left(Room):

    name = 'left'
    good_moves = ['go east', 'walk east', 'walk south', 'walk east',
                    'walk west', 'go south', 'go east', 'go west', 'go north',
                    'walk north', 'take frog', 'touch frog', 'catch frog',
                    'talk to frog']
    bad_moves = []
    intro = all_strings.left_intro
    extra = all_strings.left_extra
    bearings = all_strings.left_bearing

    def enter(self):
        self.correct_intro()
        action = self.action()

        if action == "go south" or action == "walk south":
            self.current_room = False
            return "battlefield"

        if action == "go east" or action == "walk east":
            self.current_room = False
            return "middle"

        if action == "go west" or action == "walk west":
            self.current_room = False
            return "dining room"

        if action == "go north" or action == "walk north":
            self.current_room = False
            return "butcher"

        if action == "take frog" or action == "touch frog":
            all_strings.left_take_frog()
            return self.enter()

        if action == "catch frog":
            all_strings.left_catch_frog()
            return self.enter()

        if action == 'talk to frog':
            all_strings.left_talk_frog()
            return self.enter()


class Right(Room):

    name = 'right'
    racetrack_open = True
    good_moves = ['go east', 'walk east', 'walk south', 'walk east',
                    'walk west', 'go south', 'go east', 'go west', 'go north',
                    'walk north', 'touch computer', 'touch computers',
                    'touch computer fan', 'take computer']
    bad_moves = []
    intro = all_strings.right_intro
    extra = all_strings.right_extra
    bearings = all_strings.right_bearings

    def enter(self):
        self.correct_intro()
        action = self.action()

        if action == "go south" or action == "walk south":
            self.current_room = False
            return "world"

        if (action == "go east" or action == "walk east") and self.racetrack_open:
            self.current_room = False
            return "racetrack"

        if (action == "go east" or action == "walk east" and
            not self.racetrack_open):
            all_strings.right_racetrack_closed()
            return self.enter()

        if action == "go west" or action == "walk west":
            self.current_room = False
            return "middle"

        if action == "go north" or action == "walk north":
            self.current_room = False
            return "alone"

        if action == "touch computer" or action == "touch computers":
            all_strings.right_touch_computer()
            return self.enter()

        if action == 'touch computer fan':
            all_strings.right_touch_computer_fan()
            return self.enter()

        if action == 'take computer':
            all_strings.right_take_computer()
            return self.enter()


class Battlefield(Room):

    name = 'battlefield'
    stone_here = True
    good_moves = ['go north', 'walk north', 'talk to soldier',
                'talk to her', 'touch soldier', 'take soldier', 'come closer']
    bad_moves = ['go east', 'walk east', 'walk south', 'walk west',
                'go south', 'go west', ]
    attempt_moves = ['talk to soldier', 'talk to her', 'come closer']
    intro = all_strings.battlefield_intro
    extra = all_strings.battlefield_extra_start
    bearings = all_strings.battlefield_bearings1

    bearings_final = all_strings.battlefield_bearings_final
    extra_final = all_strings.battlefield_extra_final
    room_stone = 'Stone of Respect'
    room_stone_message = all_strings.stone_of_respect_pickup

    def enter(self):

# These self.stone_available() methods are called at the beginning of each
# riddle room (except for Alone(Room)) to check if 'take stone' should be added
# to self.good_moves or not.

        self.stone_available()

# self.one_attempt_only() is present in all riddle rooms and it takes away the
# attempt_moves from a room once the riddle has been attempted

        self.one_attempt_only()

        self.correct_intro()

        action = self.action()

        if action == "go north" or action == "walk north":
            self.current_room = False
            return "left"

        if action == "take soldier":
            all_strings.battlefield_take_soldier()
            return self.enter()

        if action == "touch soldier":
            all_strings.battlefield_touch_soldier()
            return self.enter()

# This is a 'make attempt' action that is present in some form is all of the
# riddle rooms

        if (action == "talk to soldier" or
            action == "talk to her" or action == 'come closer'):

# These self.attempted attributes in the riddle rooms determine if the actual
# riddle can be started. Once attempted, no riddle can be repeated, win or lose.

            self.attempted = True
            all_strings.battlefield_riddle()
            solution = ""

# self.guesses_left is initialized as 5 for every subclass of Room

            while self.guesses_left > 0 and not self.solved:
                print """
The soldier holds up her left hand, with %d digits up.""" % self.guesses_left
                self.guesses_left -= 1
                solution = raw_input("\nHow do you answer? > ").lower().strip()

                if solution == "onion" or solution == "an onion":
                    self.solved = True

# some riddles provide a hint to help a losing player

                if self.guesses_left == 1:
                    all_strings.battlefield_hint()

            self.bearings = all_strings.battlefield_bearings2

            if self.solved:
                self.extra = all_strings.battlefield_extra_win
                all_strings.enter_to_continue()
                print all_strings.battlefield_solved

            else:
                self.extra = all_strings.battlefield_extra_fail
                print all_strings.battlefield_failed
                inv.failed_riddles += 1

# inv.end_if_failed is run after each failed riddled to see if the game-ending
# condition of 3 failures has been met and to give the player an update.

                inv.end_if_failed()

            self.intro = all_strings.battlefield_intro_final
            all_strings.enter_to_continue()

            return self.enter()

# self.stone_moves are available for all of the riddle rooms but these actions
# are only available if stone_available() at the top of self.enter() places it
# in self.good_moves.

        if action in self.stone_moves:
            return self.stone_pickup()



class DiningRoom(Room):

    name = 'dining room'
    stone_here = True
    good_moves = ['go east', 'walk east', 'read note', 'touch fountain',
                    'touch fountains', 'take fountain', 'take fountains',
                    'touch clock', 'touch grandfather clock', 'touch sofa',
                    'take sofa', 'look outside', 'touch curtains',
                    'touch curtain', 'sit on sofa', 'touch water', 'take water',
                    'take curtain', 'take curtains']
    attempt_moves = ['read note']
    bad_moves = ['go north', 'walk north', 'walk south', 'walk west',
                'go south', 'go west' ]
    intro = all_strings.dining_room_intro
    extra = all_strings.dining_room_extra_start
    bearings = all_strings.dining_room_bearings_start

    bearings_final = all_strings.dining_room_bearings_final
    extra_final = all_strings.dining_room_extra_final
    room_stone = 'Stone of Silence'
    room_stone_message = all_strings.stone_of_silence_pickup

    def enter(self):

        self.stone_available()

        self.one_attempt_only()

        self.correct_intro()

        action = self.action()

        if action == "go east" or action == "walk east":
            self.current_room = False
            return "left"

        if (action == "touch fountains" or action == "touch fountain" or
            action == "touch water" or action == "take water"):
            all_strings.dining_room_touch_water()
            return self.enter()

        if action == "take fountains" or action == "take fountain":
            all_strings.dining_room_take_water()
            return self.enter()

        if action == "touch curtains" or action == "touch curtain":
            all_strings.dining_room_touch_curtain()
            return self.enter()

        if action == "take curtains" or action == "take curtain":
            all_strings.dining_room_take_curtain()
            return self.enter()

        if action == "sit on sofa":
            dining_room_sit()
            return self.enter()

        if action == "look outside":
            all_strings.dining_room_look_outside()
            return self.enter()

        if action == "touch clock" or action == "touch grandfather clock":
            all_strings.dining_room_touch_clock()
            return self.enter()

        if (action == "take clock" or action == "take grandfather clock" or
            action == "take sofa"):
            all_strings.dining_room_take_big()
            return self.enter()

        if action == "touch sofa":
            all_strings.dining_room_touch_sofa()
            return self.enter()

# For an explanation of a general 'make attempt' action in puzzle rooms, see
# Battlefield

        if action == "read note":
            all_strings.dining_room_riddle()

            if "ballpoint pen" not in inv.items:
                all_strings.dining_room_no_pen()
                return self.enter()

# The attempt will only be made if the player is carrying 'ballpoint pen'

            elif "ballpoint pen" in inv.items:
                self.attempted = True
                all_strings.dining_room_have_pen()
                solution = ""
                while self.guesses_left > 0 and not self.solved:
                    print """
Below the note there are still %d lines that are not used up.""" % self.guesses_left
                    self.guesses_left -= 1
                    solution = raw_input("\nWhat do you write? > ").lower().strip()

                    if solution == "silence":
                        self.solved = True

                    if self.guesses_left == 1:
                        all_strings.dining_room_hint()

            self.bearings = all_strings.dining_room_bearings_after

            if self.solved:
                self.extra = all_strings.dining_room_extra_win
                all_strings.dining_room_quiet()

            else:
                self.extra = all_strings.dining_room_extra_fail
                print all_strings.dining_room_failed
                inv.failed_riddles += 1
                inv.end_if_failed()
            all_strings.dining_room_leave_pen()
            inv.remove("ballpoint pen")
            all_strings.enter_to_continue()

            return self.enter()

        if action in self.stone_moves:
            return self.stone_pickup()


class Butcher(Room):

    name = 'butcher'
    stone_here = True
    good_moves = ['go south', 'walk south', 'talk to butcher',
                    'talk to man', 'talk to him', 'touch pig', 'take meat',
                    'take cut', 'take pig', 'touch meat', 'touch cut',
                    'take cuts', 'touch cuts', 'talk to the man']
    attempt_moves = ['talk to butcher', 'talk to man',
     'talk to him']
    bad_moves = ['go north', 'walk north', 'walk east', 'walk west', 'go east',
                'go west']
    intro = all_strings.butcher_intro
    extra = all_strings.butcher_extra_start
    bearings = all_strings.butcher_bearings_start

    bearings_final = all_strings.butcher_bearings_final
    extra_final = all_strings.butcher_extra_final
    room_stone = 'Stone of Peace'
    room_stone_message = all_strings.stone_of_peace_pickup

    def enter(self):

        self.one_attempt_only()

        self.stone_available()

        self.correct_intro()

        action = self.action()

        if action == "go south" or action == "walk south":
            self.current_room = False
            return "left"

        if action == "touch pig":
            all_strings.butcher_touch_pig()
            return self.enter()

        if (action == 'touch cut' or action == 'touch meat' or
            action == 'touch cuts'):
            all_strings.butcher_touch_meat()
            for option in ['touch cut', 'touch cuts', 'touch meat']:
                self.good_moves.remove(option)
            return self.enter()

        if action == 'take pig':
            all_strings.butcher_take_pig()
            self.good_moves.remove('take pig')
            return self.enter()

        if (action == 'take meat' or action == 'take cut' or
            action == 'take cuts'):
            all_strings.butcher_take_meat()
            for option in ['take cut', 'take cuts', 'take meat']:
                self.good_moves.remove(option)
            return self.enter()

# For an explanation of a general 'make attempt' action in puzzle rooms, see
# Battlefield

        if (action == "talk to man" or
            action == "talk to butcher" or action == "talk to him" or
            action == "talk to the man"):
            self.attempted = True
            all_strings.butcher_riddle()
            solution = ""
            while self.guesses_left > 0 and not self.solved:

                if self.guesses_left == 5:
                    print """
The man uses a small knife to carve a line into the wall behind him. There is
%d line in the wall. His lips seem to curl involuntarily.""" % (6 - self.guesses_left)

                else:
                    print """
The man uses a small knife to carve a line into the wall behind him. There are
%d lines in the wall. His lips seem to curl involuntarily.""" % (6 - self.guesses_left)
                self.guesses_left -= 1
                solution = raw_input("\nHow do you answer? > ").lower().strip()

                if solution == "pillow" or solution == "a pillow":
                    self.solved = True

                if self.guesses_left == 1:
                    all_strings.butcher_hint()

# Sleep before showing player whether the answer was correct or not.

            sleep(2)
            self.bearings = all_strings.butcher_bearings_after

            if self.solved:
                self.extra = all_strings.butcher_extra_win
                print all_strings.butcher_solved

            else:
                self.extra = all_strings.butcher_extra_lose
                print all_strings.butcher_failed
                inv.failed_riddles += 1
                inv.end_if_failed()

            all_strings.enter_to_continue()

            return self.enter()

        if action in self.stone_moves:
            return self.stone_pickup()


class Racetrack(Room):

    name = 'racetrack'
    rock_on_floor = True
    stone_here = True
    good_moves = ['go west', 'walk west', 'talk', 'take rock', 'talk to robot',
                    'talk to human', 'talk to the robot', 'talk to the person',
                    'talk to the human', 'talk to human', 'talk to person',
                    'touch rock', 'take small rock', 'touch hugbot',
                    'touch robot', 'touch human', 'touch person',
                    'pick up rock', 'grab rock', 'grab small rock',
                    'pick up small rock']
    rock_moves = ['touch rock', 'take rock', 'pick up rock', 'grab rock',
                    'take small rock', 'grab small rock', 'pick up small rock']
    attempt_moves = ["throw rock", "throw rock at person",
                    "throw rock at human", "throw rock at the person",
                    "throw rock at the robot", "throw rock at robot",
                    "throw rock at hugbot", "throw rock at the human"]
    bad_moves = ['go north', 'walk north', 'walk east', 'walk south', 'go east',
                'go south']
    intro = all_strings.racetrack_intro
    extra = all_strings.racetrack_extra_start
    bearings = all_strings.racetrack_bearings_start

    bearings_final = all_strings.racetrack_bearings_final
    extra_final = all_strings.racetrack_extra_final
    room_stone = 'Stone of Friendship'
    room_stone_message = all_strings.stone_of_friendship_pickup

    def enter(self):

        if not self.rock_on_floor and not self.attempted:
            for option in self.attempt_moves:
                self.good_moves.append(option)

        self.one_attempt_only()

        self.stone_available()

        self.correct_intro()

        action = self.action()

        if action == 'go west' or action == 'walk west':
            self.current_room = False
            return 'right'

        if action == 'touch rock':
            if self.rock_on_floor:
                all_strings.racetrack_touch_rock()
                return self.enter()
            else:
                all.strings.racetrack_touch_rock_gone()
                return self.enter()

        if action == 'talk':
            all_strings.racetrack_talk()
            return self.enter()

        if action == 'touch hugbot' or action == 'touch robot':
            all_strings.racetrack_touch_robot()
            return self.enter()

        if action in self.rock_moves and action != self.rock_moves[0]:

            if self.rock_on_floor:
                self.rock_on_floor = False
                all_strings.racetrack_take_rock()
                inv.add('rock')

# Update self.extra to indicate that the rock is no longer there.

                self.extra = all_strings.racetrack_extra_no_rock
                return self.enter()

# Can't pick up the rock if it's not there.

            else:
                all_strings.racetrack_take_rock_gone()
                return self.enter()

        if action == 'throw rock':
            all_strings.racetrack_throw_rock()
            return self.enter()

        if action == 'talk to robot' or action == 'talk to the robot':
            for option in ['talk to robot', 'talk to the robot']:
                self.good_moves.remove(option)
            all_strings.racetrack_talk_to_robot()

            return self.enter()

        if (action == 'talk to human' or action == 'talk to the human' or
            action == 'talk to person' or action == 'talk to the person' or
            action == 'touch human' or action == 'touch person'):
            all_strings.racetrack_talk_to_human()

            return self.enter()

# This is another kind of 'make attempt' that can only lead to failure.

        if action == "throw rock at human" or action == "throw rock at person":
            inv.remove('rock')
            self.attempted = True
            all_strings.racetrack_throw_rock_at_human()
            inv.failed_riddles += 1
            inv.end_if_failed()
            right_room.racetrack_open = False
            return "right"

# For an explanation of a general 'make attempt' action in puzzle rooms, see
# Battlefield

        if (action == "throw rock at robot" or
        action == "throw rock at the robot" or
        action == "throw rock at hugbot"):
            inv.remove('rock')
            self.attempted = True
            all_strings.racetrack_riddle()

# robot_clock is just used to create a series of numbers that counts down in
# multiples of itself to indicate to the player that there are a finite number
# of attempts left (presumably, when the timer reaches 0, no more guesses will
# be allowed.)

            robot_clock = randint(1500, 1900)

            while self.guesses_left > 0 and not self.solved:
                self.guesses_left -= 1
                print """
'It's okay my friend, you are loved,' the hugbot says. You see the number %d
quickly counting down on the display that's (gently) pressing into your face.
""" % (((self.guesses_left + 1) * robot_clock) + randint(1, 100))
                solution = raw_input("What is the safeword? > ").lower().strip()

                if solution == "fork" or solution == "a fork":
                    self.solved = True

                if self.guesses_left == 1:
                    all_strings.racetrack_hint()

            self.bearings = all_strings.racetrack_bearings_after

            if self.solved:
                self.extra = all_strings.racetrack_extra_win
                all_strings.racetrack_solved()

            else:
                self.extra = all_strings.racetrack_extra_lose
                print all_strings.racetrack_failed
                inv.failed_riddles += 1
                inv.end_if_failed()

            all_strings.enter_to_continue()
            return self.enter()

        if action in self.stone_moves:
            return self.stone_pickup()


class Alone(Room):

    name = 'alone'

# This room has a lot of attributes due to a more intricate system of what
# messages display at any given time and also a projector that has a number of
# potential states

    final_response = False
    good_text_up = False
    sad_text_up = False
    projector_power = False
    projector_on = False
    projector_open = False
    stone_here = True
    looked = False
    good_moves = ['go south', 'walk south', 'talk to lady',
                    'talk to her', 'talk to woman', 'talk to projector',
                    'talk to girl', 'plug in projector', 'turn on projector',
                    'open lid', 'open projector lid', 'look at projector',
                    'turn off projector', 'look at the projector', 'close lid',
                    'close projector lid', 'turn on the projector',
                    'turn off the projector', 'plug in the projector',
                    'unplug the projector', 'talk to the projector',
                    'unplug projector', 'look under projector',
                    'look under the projector', 'inspect projector']
    bad_moves = ['go north', 'walk north', 'walk east', 'walk west', 'go east',
                'go west']
    intro = all_strings.alone_intro
    extra = all_strings.alone_extra_start
    bearings = all_strings.alone_bearings_start

    bearings_final = all_strings.alone_bearings_final
    extra_final = all_strings.alone_extra_final
    room_stone = 'Stone of Compassion'
    room_stone_message = all_strings.stone_of_compassion_pickup

    def enter(self):

# This is in essence the same thing as the stone_available() method from Room()
# but it also checks self.looked.

        if (self.solved and self.stone_here and
         self.stone_moves[0] not in self.good_moves and self.looked):
            for option in self.stone_moves:
                self.good_moves.append(option)
        if not self.stone_here and self.stone_moves[0] in self.good_moves:
            for option in self.stone_moves:
                self.good_moves.remove(option)

        self.correct_intro()

# This is used to control a message that comes up in self.extra, but it is not
# necessary and should be refactored so that the message just uses
# self.stone_here. This final_response message overrides all other self.extra
# messages
        if not self.stone_here:
            self.final_response = True

# This is a unique implementation of the 'make attempt' as defined in
# Battlefield(Room). It plays only when the state of three projector attributes
# are True and doesn't require any direct action from the player to run,
# otherwise it is basically the same thing as the other 'make attempt' pieces.
#
# self.loading() is defined at the bottom of Alone(Room) and is a variation of
# time.sleep() that prints dots every second.

        if (self.projector_on and self.projector_open and not self.attempted):
            self.attempted = True
            all_strings.alone_riddle()
            while self.guesses_left > 0 and not self.solved:

# self.loading here is used to give the player a sense that there is a limited
# number of guesses that can be made as it prints progressively fewer dots
# between guesses.

                self.loading(self.guesses_left)
                self.guesses_left -= 1
                solution = raw_input("\n?? > ").lower().strip()

                if solution == "shoe" or solution == "a shoe":
                    self.solved = True

                if self.guesses_left == 1:
                    all_strings.alone_hint()

# self.good_text_up and self.sad_text_up exist because the projector can be
# turned off, in which event a different self.extra will be loaded. If
# self.good_text_up or self.sad_text_up then these will display as self.extra
# if the projector is then turned back on.

            if self.solved:
                self.good_text_up = True
                self.extra = all_strings.alone_extra_win
                all_strings.alone_solved()

            else:
                self.sad_text_up = True
                self.extra = all_strings.alone_extra_lose
                all_strings.alone_failed()
                inv.failed_riddles += 1
                inv.end_if_failed()

            all_strings.enter_to_continue()
            return self.enter()

        action = self.action()

        if action == "go south" or action == "walk south":
            self.current_room = False
            return "right"

        if (action == "talk to lady" or
            action == "talk to her" or action == "talk to woman"):
            all_strings.alone_talk_to_lady()
            return self.enter()

        if action == "talk to projector" or action == "talk to the projector":
            all_strings.alone_talk_to_projector()
            return self.enter()

        if action == "talk to girl":
            all_strings.alone_talk_to_girl()
            return self.enter()

        if action == "plug in projector" or action == "plug in the projector":

# If the projector is already plugged in, get a different message.

            if self.projector_power:
                all_strings.alone_projector_powered()
                return self.enter()

# If self.final response is up it supersedes all other possible changes to
# self.extra

            if self.final_response:
                self.extra = all_strings.alone_extra_final

# If the riddle has been attempted and failed, a particular message will be
# self.extra when the projector is replugged in

            elif self.attempted and not self.solved:
                self.extra = all_strings.alone_extra_proj_power_failed

# If the projector is plugged in but it is not on:

            elif not self.final_response and not self.projector_on:
                self.extra = all_strings.alone_extra_proj_power_off

            self.projector_power = True
            all_strings.alone_projector_power_on()
            return self.enter()

        if action == "unplug projector" or action == "unplug the projector":

# If the projector is already unpluged, get a different message.

            if not self.projector_power:
                all_strings.alone_projector_unpowered()
                return self.enter()
            self.projector_power = False
            self.projector_on = False
            all_strings.alone_projector_power_off()

# If the riddle has been attempted and failed, a particular message will be
# self.extra when the projector is uplugged in

            if self.attempted and not self.solved:
                self.extra = all_strings.alone_extra_proj_unplug_failed

# As long as the final response is not up, the following self.extra will play:

            elif not self.final_response:
                self.extra = all_strings.alone_extra_proj_unplug

            return self.enter()

        if action == "turn on projector" or action == "turn on the projector":

# If projector was already on:

            if self.projector_on:
                all_strings.alone_projector_running()
                return self.enter()

# Turn on projector

            if self.projector_power:
                all_strings.alone_projector_turn_on()
                self.projector_on = True

# self.final_response supersedes all other self.extra messages

                if self.final_response:
                    self.extra = all_strings.alone_extra_final

# Only one of either self.good_text_up or self.sad_text_up would be True in any
# one game and they will only replace self.extra if the projector lid is open.

                elif self.good_text_up and self.projector_open:
                    self.extra = all_strings.alone_extra_win

                elif self.sad_text_up and self.projector_open:
                    self.extra = all_strings.alone_extra_lose

# If we're not at the final response and the lid is closed, we get this:

                elif not self.final_response:
                    self.extra = all_strings.alone_extra_proj_on_closed

                return self.enter()

# Projector can't be turned on if it is not plugged in:

            elif not self.projector_power:
                all_strings.alone_projector_no_power()
                return self.enter()

        if action == "turn off projector" or action == "turn off the projector":

# If the projector is already off:

            if not self.projector_on:
                all_strings.alone_projector_was_off()
                return self.enter()

# Turn projector off:

            self.projector_on = False
            all_strings.alone_projector_turn_off()

# If the riddle has been attempted and failed:

            if self.attempted and not self.solved:
                self.extra = all_strings.alone_extra_proj_off_failed

# As long as we're not at the final response we get the following message:

            elif not self.final_response:
                self.extra = all_strings.alone_extra_proj_off

            return self.enter()

        if (action == 'look at projector' or action == 'look at the projector' or
            action == 'inspect projector'):
            all_strings.alone_proj_look_basic()

# List state of main 3 projector attributes

            if not self.projector_open:
                all_strings.alone_proj_look_lid()

            if not self.projector_on:
                all_strings.alone_proj_look_on()

            if not self.projector_power:
                all_strings.alone_proj_look_power()

            return self.enter()

        if action == "open lid" or action == "open projector lid":

            if self.projector_open:
                all_strings.alone_projector_no_lid()
                return self.enter()

# self.final_response supersedes all other possible self.extra messages

            if self.final_response:
                self.extra = all_strings.alone_extra_final

# These will only replace self.extra if the projector is actually on.

            elif self.good_text_up and self.projector_on:
                self.extra = all_strings.alone_extra_win

            elif self.sad_text_up and self.projector_on:
                self.extra = all_strings.alone_extra_lose

# If the projector is off we get:

            elif not self.final_response:
                self.extra = all_strings.alone_extra_proj_opened_off

            self.projector_open = True
            all_strings.alone_projector_open()
            return self.enter()

        if action == "close lid" or action == "close projector lid":

# If lid is already closed:

            if not self.projector_open:
                all_strings.alone_projector_lid()
                return self.enter()

# If the riddle is failed:

            if self.attempted and not self.solved:
                self.extra = all_strings.alone_extra_proj_closed_failed

# In any other circumsntance apart from self.final_response being true:

            elif not self.final_response:
                self.extra = all_strings.alone_extra_proj_closed

# Close projector lid:

            self.projector_open = False
            all_strings.alone_projector_close()
            return self.enter()

        if (action == "look under projector" or
        action == "look under the projector"):

# If the puzzle isn't solved (attempted or not):

            if not self.solved:
                all_strings.alone_look_under_start()
                return self.enter()

# If the puzzle is solved and the stone hasn't been taken:

            elif self.stone_here and self.solved:
                self.looked = True
                all_strings.alone_look_under_solved()
                return self.enter()

# If the stone has been taken:

            else:
                all_strings.alone_look_under_final()
                return self.enter()

        if action in self.stone_moves:
            return self.stone_pickup()

# This is the modified sleep function used in the "make attempt" action in this
# room

    def loading(self, count):
        for i in xrange(count):
            sleep(1)
            print "\n."


class World(Room):

    name = 'world'
    stone_here = True
    good_moves = ['go north', 'walk north', 'talk to elephant',
                'talk to it', 'sit', 'sit cross-legged', 'sit on rock',
                'touch elephant', 'touch rock', 'talk to rock',
                'enjoy the view', 'look at mountains', 'fan yourself',
                'enjoy the amazing view', 'enjoy view', 'look at view']
    attempt_moves = ['talk to elephant', 'talk to it']
    bad_moves = ['go east', 'walk east', 'walk south', 'walk west',
                'go south', 'go west', ]
    intro = all_strings.world_intro_start
    extra = all_strings.world_extra_start
    bearings = all_strings.world_bearings

    bearings_final = all_strings.world_bearings
    extra_final = all_strings.world_extra_final
    room_stone = 'Stone of Practice'
    room_stone_message = all_strings.stone_of_practice_pickup

    def enter(self):

        self.one_attempt_only()

        self.stone_available()

        self.correct_intro()

        action = self.action()

        if action == "go north" or action == "walk north":
            self.current_room = False
            return "right"

        if action == "sit":

            if self.stone_here:
                all_strings.world_sit_start()
                return self.enter()

            else:
                all_strings.world_sit_final()
                return self.enter()

        if action == "sit cross-legged":

            if self.stone_here:
                all_strings.world_meditate_start()
                return self.enter()

            else:
                all_strings.world_meditate_final()
                return self.enter()

        if action == "sit on rock":

            if self.stone_here:
                all_strings.world_chill_start()
                return self.enter()

            else:
                all_strings.world_chill_final()
                return self.enter()

        if (action == "enjoy the view" or action == "enjoy the amazing view" or
            action == "enjoy view" or action == "look at view"):

            if self.stone_here:
                all_strings.world_enjoy_start()
                return self.enter()

            else:
                all_strings.world_enjoy_final()
                return self.enter()

        if action == "look at mountains":

            if self.stone_here:
                all_strings.world_gaze_start()
                return self.enter()

            else:
                all_strings.world_gaze_final()
                return self.enter()

        if action == "touch rock":

            if self.stone_here:
                all_strings.world_rock_start()
                return self.enter()

            else:
                all_strings.world_rock_final()
                return self.enter()

        if action == "talk to rock":

            if self.stone_here:
                all_strings.world_rock_buddy_start()
                return self.enter()

            else:
                all_strings.world_rock_buddy_final()
                return self.enter()

        if action == "fan yourself":

            if self.stone_here:
                all_strings.world_fan_start()
                return self.enter()

            else:
                all_strings.world_fan_final()
                return self.enter()

        if action == "touch elephant":
            all_strings.world_touch()
            return self.enter()

# For an explanation of a general 'make attempt' action in puzzle rooms, see
# Battlefield

        if (action == "talk to elephant" or
            action == "talk to it"):
            self.attempted = True
            all_strings.world_riddle()
            while self.guesses_left > 0 and not self.solved:
                sleep(1)
                self.overheating(self.guesses_left)
                self.guesses_left -= 1
                sleep(1)
                solution = raw_input("\nYou speak > ").lower().strip()

                if solution == "ton":
                    self.solved = True

            if self.solved:
                self.extra = all_strings.world_extra_win
                sleep(1)
                print all_strings.world_solved

            else:
                self.extra = all_strings.world_extra_lose
                print all_strings.world_failed
                inv.failed_riddles += 1
                inv.end_if_failed()

            all_strings.enter_to_continue()
            self.intro = all_strings.world_intro_final
            return self.enter()

        if action in self.stone_moves:
            return self.stone_pickup()

    def overheating(self, count):
        if count == 5:
            print all_strings.world_overheating1
        if count == 4:
            print all_strings.world_overheating2
        if count == 3:
            print all_strings.world_overheating3
        if count == 2:
            print all_strings.world_overheating4
        if count == 1:
            print all_strings.world_overheating5
        if count == 0:
            print all_strings.world_overheating6


class End(Room):

    name = 'end'
    stories = {
    'Stone of Peace': all_strings.stone_of_peace_message,
    'Stone of Silence': all_strings.stone_of_silence_message,
    'Stone of Respect': all_strings.stone_of_respect_message,
    'Stone of Practice': all_strings.stone_of_practice_message,
    'Stone of Friendship': all_strings.stone_of_friendship_message,
    'Stone of Compassion': all_strings.stone_of_compassion_message}

    def enter(self):
        all_strings.end_start()
        for stone in door_room.stones.keys():

# If player placed the stone in indentations in door_room they will get the
# corresponding message

            if door_room.stones[stone]:
                raw_input("Go on? > ")
                print "\nYou found the %s." % stone
                print self.stories[stone]
                print "\n" * 2

        raw_input("Ready to finish? > ")
        print all_strings.end_message
        exit(1)

# These Room objects are necessary as they allow the Saver to get the current
# state of each of the rooms

start_room = StartingRoom()
middle_room = MiddleRoom()
door_room = TheDoor()
left_room = Left()
right_room = Right()
butcher_room = Butcher()
dining_room = DiningRoom()
battlefield_room = Battlefield()
racetrack_room = Racetrack()
alone_room = Alone()
world_room = World()
end_room = End()

class Map(object):

# This maps a string that is the output of these room objects' .enter() method
# and uses it to find the next room that will be entered.

    rooms = {'start': start_room, 'middle': middle_room, 'door': door_room,
            'left': left_room, 'right': right_room, 'butcher': butcher_room,
            'dining room': dining_room, 'battlefield': battlefield_room,
            'racetrack': racetrack_room, 'alone': alone_room,
            'world': world_room, 'end': end_room}

# This method gets called by Engine and keeps getting called until the end_room
# is reached.

    def play(self, next_room):

# The 35 next lines are used to break the rooms up from one another on the
# display.

        print "\n" * 35
        return self.rooms[next_room].enter()


class Saver(object):

    rooms = {'start': start_room, 'middle': middle_room, 'door': door_room,
            'left': left_room, 'right': right_room, 'butcher': butcher_room,
            'dining room': dining_room, 'battlefield': battlefield_room,
            'racetrack': racetrack_room, 'alone': alone_room,
            'world': world_room}

    riddle_rooms = ['butcher', 'dining room', 'battlefield', 'racetrack',
                    'alone', 'world']

# Saver gets initialized in the save action inside Room(object), the room and
# inv objects from this file are used as the arguments along with the name of
# the specific room object from which it is called (current)

    def __init__(self, start, middle, door, left, right, battle,
                dining, butcher, alone, race, world, inv, current):
        self.start = start
        self.middle = middle
        self.door = door
        self.left = left
        self.right = right
        self.battle = battle
        self.dining = dining
        self.butcher = butcher
        self.alone = alone
        self.race = race
        self.world = world
        self.inv = inv
        self.current = current

# A SavedGame object holds all the attributes that change the state of the game
# as instance variables. save() then takes all the room objects that it was
# instantiated with and passes their attributes into this stock SavedGame file
# (which initially hold values that are identical to the start of game values
# found in this file.)

    def save(self):
        save_file = SavedGame()
        save_file.items = self.inv.items
        save_file.starting = self.current
        save_file.failed_riddles = self.inv.failed_riddles

# This loop deals with assigning all common room attributes

        for room in self.rooms.keys():
            save_file.rooms[room]['intro'] = self.rooms[room].intro
            save_file.rooms[room]['bearings'] = self.rooms[room].bearings
            save_file.rooms[room]['extra'] = self.rooms[room].extra
            save_file.rooms[room]['visited'] = self.rooms[room].visited

# Same as above but it only deals with the riddle rooms that have their own
# common attributes

        for room in self.riddle_rooms:
            save_file.rooms[room]['solved'] = self.rooms[room].solved
            save_file.rooms[room]['attempted'] = self.rooms[room].attempted
            save_file.rooms[room]['stone_here'] = self.rooms[room].stone_here

# Make sure that any stones placed in the_door are stored in the save_file

        for stone in self.door.stones.keys():
            save_file.rooms['door'][stone] = self.door.stones[stone]

# Assorted other important attributes

        save_file.rooms['start']['start_of_game'] = self.start.start_of_game
        save_file.rooms['start']['pen'] = self.start.pen
        save_file.rooms['door']['door_open'] = self.door.door_open
        save_file.rooms['door']['attempted_door'] = self.door.attempted_door
        save_file.rooms['door']['touched_indentations'] = self.door.touched_indentations
        save_file.rooms['door']['bag_here'] = self.door.bag_here
        save_file.rooms['right']['racetrack_open'] = self.right.racetrack_open
        save_file.rooms['racetrack']['rock_on_floor'] = self.race.rock_on_floor
        save_file.rooms['alone']['final_response'] = self.alone.final_response
        save_file.rooms['alone']['good_text_up'] = self.alone.good_text_up
        save_file.rooms['alone']['sad_text_up'] = self.alone.sad_text_up
        save_file.rooms['alone']['projector_power'] = self.alone.projector_power
        save_file.rooms['alone']['projector_on'] = self.alone.projector_on
        save_file.rooms['alone']['projector_open'] = self.alone.projector_open
        save_file.rooms['alone']['looked'] = self.alone.looked

        return save_file


class Loader(object):

    rooms = {'start': start_room, 'middle': middle_room, 'door': door_room,
            'left': left_room, 'right': right_room, 'butcher': butcher_room,
            'dining room': dining_room, 'battlefield': battlefield_room,
            'racetrack': racetrack_room, 'alone': alone_room,
            'world': world_room}

    riddle_rooms = ['butcher', 'dining room', 'battlefield', 'racetrack',
                    'alone', 'world']

# Loader gets instantiated with a save file (unpickled from saved.py) and the
# inventory object (the inv that is instantiated in this save file)

    def __init__(self, save, inventory):
        self.info = save
        self.inv = inventory

    def load_it(self):

# The inv object instantiated in this game file gets the save file's inventory
# items and number of failed riddles.

        self.inv.items = self.info.items
        self.inv.failed_riddles = self.info.failed_riddles

# Same as with Saver

        for room in self.rooms.keys():
            self.rooms[room].visited = self.info.rooms[room]['visited']
            self.rooms[room].intro = self.info.rooms[room]['intro']
            self.rooms[room].extra = self.info.rooms[room]['extra']
            self.rooms[room].bearings = self.info.rooms[room]['bearings']

        for room in self.riddle_rooms:
            self.rooms[room].solved = self.info.rooms[room]['solved']
            self.rooms[room].attempted = self.info.rooms[room]['attempted']
            self.rooms[room].stone_here = self.info.rooms[room]['stone_here']

        for stone in door_room.stones.keys():
            door_room.stones[stone] = self.info.rooms['door'][stone]

        start_room.start_of_game = self.info.rooms['start']['start_of_game']
        start_room.pen = self.info.rooms['start']['pen']
        door_room.door_open = self.info.rooms['door']['door_open']
        door_room.attempted_door = self.info.rooms['door']['attempted_door']
        door_room.touched_indentations = self.info.rooms['door']['touched_indentations']
        door_room.bag_here = self.info.rooms['door']['bag_here']
        right_room.racetrack_open = self.info.rooms['right']['racetrack_open']
        racetrack_room.rock_on_floor = self.info.rooms['racetrack']['rock_on_floor']
        alone_room.final_response = self.info.rooms['alone']['final_response']
        alone_room.good_text_up = self.info.rooms['alone']['good_text_up']
        alone_room.sad_text_up = self.info.rooms['alone']['sad_text_up']
        alone_room.projector_power = self.info.rooms['alone']['projector_power']
        alone_room.projector_on = self.info.rooms['alone']['projector_on']
        alone_room.projector_open = self.info.rooms['alone']['projector_open']
        alone_room.looked = self.info.rooms['alone']['looked']

        return self.info.starting


class SavedGame(object):

# This class is used to collect all the attributes that are necessary to keep
# track of in order to know the state of the game at the time of the save. This
# file is then pickled to saved.py and is then unpickled and fed into the Loader
# if the player wants to load the values from the save into the current game

    def __init__(self):
        self.items = []
        self.failed_riddles = 0
        self.starting = "start"
        self.rooms = {"start":
                                {'pen': True, 'visited': True,
                                'start_of_game': True,
                                'intro': all_strings.starting_room_intro,
                                'extra': all_strings.starting_room_extra1,
                                'bearings': all_strings.starting_room_bearings1},
                        "middle":
                                {'visited': False,
                                'intro': all_strings.middle_room_intro,
                                'extra': all_strings.middle_room_extra,
                                'bearings': all_strings.middle_room_bearings},
                        "door":
                                {'visited': False,
                                'door_open': False, 'attempted_door': False,
                                'touched_indentations': False, 'bag_here': True,
                                'intro': all_strings.the_door_intro,
                                'extra': all_strings.the_door_extra1,
                                'bearings': all_strings.the_door_bearings1,
                                'Stone of Peace': False, 'Stone of Silence': False,
                                'Stone of Respect': False,
                                'Stone of Practice': False,
                                'Stone of Friendship': False,
                                'Stone of Compassion': False},
                        "left":
                                {'visited': False,
                                'intro': all_strings.left_intro,
                                'extra': all_strings.left_extra,
                                'bearings': all_strings.left_bearing},
                        "right":
                                {'visited': False,
                                'racetrack_open': True,
                                'intro': all_strings.right_intro,
                                'extra': all_strings.right_extra,
                                'bearings': all_strings.right_bearings},
                        "battlefield":
                                {'visited': False,
                                'solved': False, 'stone_here': True,
                                'attempted': False,
                                'intro': all_strings.battlefield_intro,
                                'extra': all_strings.battlefield_extra_start,
                                'bearings': all_strings.battlefield_bearings1},
                        "dining room":
                                {'visited': False, 'solved': False,
                                'stone_here': True, 'attempted': False,
                                'intro': all_strings.dining_room_intro,
                                'extra': all_strings.dining_room_extra_start,
                                'bearings': all_strings.dining_room_bearings_start},
                        "butcher":
                                {'visited': False, 'attempted': False,
                                'solved': False, 'stone_here': True,
                                'intro': all_strings.butcher_intro,
                                'extra': all_strings.butcher_extra_start,
                                'bearings': all_strings.butcher_bearings_start},
                        "racetrack":
                                {'visited': False,
                                'solved': False, 'stone_here': True,
                                'rock_on_floor': True, 'attempted': False,
                                'intro': all_strings.racetrack_intro,
                                'extra': all_strings.racetrack_extra_start,
                                'bearings': all_strings.racetrack_bearings_start},
                        "alone":
                                {'solved': False, 'visited': False,
                                'stone_here': True, 'final_response': False,
                                'good_text_up': False, 'sad_text_up': False,
                                'projector_power': False, "projector_on": False,
                                "projector_open": False, "attempted": False,
                                "looked": False,
                                'intro': all_strings.alone_intro,
                                'extra': all_strings.alone_extra_start,
                                'bearings': all_strings.alone_bearings_start},
                        "world":
                                {'solved': False, 'visited': False,
                                'stone_here': True, 'attempted': False,
                                'intro': all_strings.world_intro_start,
                                'extra': all_strings.world_extra_start,
                                'bearings': all_strings.world_bearings}}

# This if statement is just so that the game does run if it was imported as a
# module into another script.

if __name__ == "__main__":
    the_map = Map()

# Get the SavedGame object from saved.py. If there is no saved.py, get a stock
# SavedGame file in case the player chooses to 'load' regardless.

    try:
        with open('saved.py', 'rb') as loaded_doc:
            load_game = pickle.load(loaded_doc)
    except IOError:
        load_game = SavedGame()

    inv = Inventory()
    loader = Loader(load_game, inv)
    game = Engine(the_map, loader)
    game.play()

# TODO: Refactor stone_here and final_response in Alone(Room) to get rid of
# final_response entirely
