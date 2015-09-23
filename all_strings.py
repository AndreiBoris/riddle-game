from time import sleep

action_go = "\nWhere to go?\n"

action_lie = "\nHere? I think not!\n"

action_prompt = "\nWhat do you do? \n"

action_sit = "\nYou'd rather stand.\n"

action_sleep = "\nYou don't feel tired enough.\n"

action_stand = "\nBeen there, done that.\n"

action_take = "\nTake! Take! Take! Do you even know what you want?\n"

action_touch = "\nFeel.\n"

action_wait = "\nWhy wait?\n"

action_walk = "\nYou pace around the room and end up where you started.\n"

bad_moves = "\nYou can't go there from here.\n"

empty_inv = "Just the clothes on your back."

helper = """
Here are some actions that you might be able to take:

- walk (somewhere)
- inventory (or inv)
- look around (or look)
- intro
- touch (something)
- take (something)
- place (something)
- throw (something)

Perhaps looking around can help you find some other possible actions to take?
"""

line_break = "--------------------------------"

lose_game = """
None of these rooms seem to make any sense. 'Why am I here?!' you call out.
You receive no answer. You have no answer. There is nothing."""

middle_room_bearings ="""
To the north there is a door that is in incongruously good condition. To the
east is some sort of office wing. To the west there is a dark tunnel. To the
south is a short hallway leading to a small apartment room.

What do you do?\n"""

middle_room_extra ="""
The smell of singed hair and old rubber is not exactly comforting."""

middle_room_intro = """
This room is huge - remarkably so. It makes one wonder what kind of building was
designed to hold such a mammoth. Despite its awe-inspiring size, the upkeep
leaves much to be desired. It dripping with old newspapers that have been left
lying around and in various makeshift beddings. Dripping because the ceiling is
soaked - evidently the roof doesn't do such a great job keeping the rain out."""

def middle_room_take_newspaper():
    print """
As you pick up a newspaper up, it falls apart in your hand in a sloppy mess."""
    sleep(2.5)
    print """
It hits the ground with a wet sound."""
    sleep(1.5)

def middle_room_take_rubber():
    print "\nSomehow you don't think it will come in handy."
    sleep(1.5)

def middle_room_touch_newspaper():
    print "\nSoggy.\n"
    sleep(1.5)

def middle_room_touch_rubber():
    print "\nUh... no."
    sleep(1.5)

room_bearings = """
There appears to be no way to get your bearings in this generic room.

What do you do?
"""

starting_room_bearings1 = """
There is some junk lying around. There is a hallway to the north.

What do you do?\n"""

starting_room_extra1 = """
This looks like the sloppy apartment of a bachelor. How lovely.

There appears to be a pen on the floor near to the mattress."""

starting_room_extra2 ="""
This looks like the sloppy apartment of a bachelor. How lovely.

The rest of the junk on the floor is junk."""

starting_room_intro = """
This is the room you woke up in. Apart from the spartan set up and the random
mattress placement, it's not so bad."""

def starting_room_lie():
    print """
You're not sure what made you pass out in this room in the first place, but once
was probably enough."""
    sleep(3)

def starting_room_take_junk():
    print """
Probably best to not hoard a bunch of junk. Maybe there is something useful
around here?"""
    sleep(3)

def starting_room_take_mattress():
    print """
As you get ready to pick the whole thing up, you're struck that maybe the
mattress is perfectly fine being just where it is."""
    sleep(3)

def starting_room_take_pen():
    print """
You pick up the pen. It is a blue ballpoint. Can never have enough pens."""
    sleep(2)

def starting_room_touch_junk():
    print """
There is so much junk to choose from, you don't know where to begin. You do
nothing."""
    sleep(3)

def starting_room_touch_mattress():
    print """
Springs. Notably mediocre."""
    sleep(3)

def starting_room_touch_pen():
    print """
Your clumsy fingers cause the pen to slide away from you."""
    sleep(2)
    print "\nUgh."
    sleep(2)

starting_room_wake_up = """You wake up.

Your mind is foggy but slowly you get your bearings.

You are in a blue-tinted room surrounded by what seems to be drywall. You are
lying on a mattress sprawled in the middle of the room. You're dressed normally.
Nothing seems to have gone wrong but you don't have a clear idea of where you
are or why."""

talking = ["'Yes, I am talking'", "'I know English.'", "'Words words words.'",
            "'Can I stop talking now?'",
            "'Am I supposed to say anything in particular?'", "'La la la.'",
            "'The power of human expression is being tapped right now.'",
            "'I don't have a whole lot more that I can say.'", "'Yup.'",
            "'Good. Good.'", "'Lovely weather...'"]

touch_stone = "\nHard.\n"
