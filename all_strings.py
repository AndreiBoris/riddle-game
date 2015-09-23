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

left_bearing = """
To the north appears to be a butcher shop. To the west you see the glimmer of a
upperclass dining room, complete with fine china and ornamental lamps. The the
south are some sort of ruins, seemingly made by a bomb explosion. To the east is
the dumpy, drippy room.

What do you do?\n"""

def left_catch_frog():
    print """
You wander in the darkness trying to echo-locate the frog."""
    sleep(3)
    print """
The frog has fallen annoying silent."""
    sleep(2)

left_extra = """
The sounds made by a croaking frog are somehow comforting. Why it is here, you
do not ask, only that you are not alone and perhaps the world is not as scary
a place as you once thought it was."""

left_intro = """
After walking through the dark tunnel for a while you begin to feel quite
certain of one thing: it is very dark here. Not that that's a problem or
anything. Though if it wasn't for the faint glimmers of other places peaking
through in the distance you would probably begin to lose your mind right now
about. Hey, maybe you'll be doing that regardless, why not!"""

def left_take_frog():
    print """
You would have to catch it first."""
    sleep(2)

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

right_bearings = """
To the north appears to be another bachelor's apartment. You wonder what the
rent is around this place. To the east seems to be the entryway to a racetrack.
The south is an opening leading to the top of a mountain. Whoa. To the west is
that large sack of moist newspapers that might be called a great hall.

What do you do?\n"""

right_extra = """
There are a bunch of computers that you wouldn't mind touching. The sounds of
computer fans are oddly calming. """

right_intro = """
Wow. A totally intact office. There are even a bunch of computers, some of
which are just idling. As you walk by desktops and laptops you feel a growing
lack of fulfillment. The desire to throw the computers across the room and dance
in the wreakage grows stronger and stronger. But no. You mustn't. You love
technology. You need it. You feel certain of this. You begin to let go.
Surrender. Everything will be okay."""

def right_racetrack_closed():
    print """
You start walking toward the racetrack when you realize what awaits you there
after that episode with the rock and the human ... Perhaps it is best to just
stay right where you are."""
    sleep(3)

def right_touch_computer():
    print """
You walk up to one of the computers with the intention to check your e-mail or
watch some YouTube videos or something."""
    sleep(4)
    print """
It seems like the computer is sleeping, so you give the mouse a shake."""
    sleep(3)
    print "\nIt works!"
    sleep(3)
    print "\nHmmm, it seems like all the networks works are passworded."
    sleep(4)
    print "\nAfter trying a few easy ones, you decide it is hopeless."
    sleep(4)

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

the_door_already_open = """
Good thing the door is already open. You felt certain that another struggle with
an opponent this powerful would have resulted in grievious injury."""

def the_door_experienced():
    print """
Using your past failure to open the door to your advantage, you waste no time
and pull on the door after turning the handle."""
    sleep(4)
    print "\nSuccess!"
    sleep(1.5)

the_door_bearings1 = """
An immaculate door is just to the north of you. Behind you, to the south, is the
big, dripping room.

What do you do?\n"""

the_door_bearings2 = """
The immaculate door is open! Beyond it, to the north, is one of those weird
foggy screens that you can't see behind but can probably walk through without
getting terribly hurt. Behind you, to the south, is the big, dripping room.

What do you do?\n"""

def the_door_believe():
    print "\n'Believe,' you whisper to yourself and march toward the door."
    sleep(3)
    print "\n'Ouch!'"
    sleep(2.5)
    print """
Yes, this door really is there. Maybe it's worth trying to open it before
attempting to channel Houdini some more."""
    sleep(3.5)

def the_door_can_pull():
    print "In a desperate effort, you pull on the door handle."
    sleep(2)
    print "\nNice."
    sleep(2)
    print "\nThe door is now open."
    sleep(1.5)

def the_door_cant_push():
    print """
You turn the handle and give the door a good push. Nothing. What? But the
stones! You had hoped that this would be enough?"""
    sleep(4)
    print "\nWhat is missing? What needs be done?"
    sleep(3)
    print "\nYour mind spins around in despair..."
    sleep(4)

the_door_extra1 = """
There is a bag made out of fabric on the floor next to the door. It is seriously
messing up how cool this door looks.

The door looks so beautiful that you would love to touch it, not that you'd
expect to learn anything. There are also some slightly more useful looking
indentations that are within reach."""

the_door_extra2 = """
Ah, good! That dirty bag is no longer messing up the look of the sweet, sweet
door. All is well.

The door looks so beautiful that you would love to touch it, not that you'd
expect to learn anything. There are also some more useful looking indentations
that are within reach."""

the_door_intro = """
This door is incredible. It is probably the best door you have ever seen.
Picture the nicest door you ever saw. That's what this looks like. It has three
indentations to either side of it."""

def the_door_struggles():
    print """
You turn the handle and give the door a good push. Nothing. You give up,
defeated."""
    sleep(4)
    print """
'Of course! This door is a pull!' you say. You turn the handle and triumphantly
pull on the door!"""
    sleep(5)
    print "\nNope. Definitely not opening. At least you gave it your all!"
    sleep(2.5)
    print "\n(It wasn't enough.)"
    sleep (1.5)

def the_door_take_indentations():
    print "\nIt would be very impressive if you could actually do that."
    sleep(3)

def the_door_touch_indentations1():
    print "\nThese indentations are cold."
    sleep(2)

def the_door_have_stone():
    print """
It seems like a stone that you have might fit into one of these indentations.
Maybe you could try placing the stone?"""
    sleep(3.5)

def the_door_no_stone():
    print """
You wonder what these indentations might be for. Perhaps they are meant to hold
something? But what? You'll have to look around."""
    sleep(3)

def the_door_not_placed():
    print """
You pull out a stone and get ready to place it on the wall. Except in your hand
there is nothing at all. It is empty. How silly of you."""
    sleep(4)

def the_door_take_bag():
    print """
There is something sticky under the bag so you have to really give it a tug
before you can lift it up."""
    sleep(3)
    print """
Upon closer inspection, it doesn't look half bad! Rough, rugged, tough, serious.
The bag reminds you enough of your childhood that you think it's best if you
hold onto it. Might come in handy."""
    sleep(6)

def the_door_touch_door():
    print "\nNo door has the right to feel this good."
    sleep(3)
    print "\nReluctantly, you back away."
    sleep(2)

touch_stone = "\nHard.\n"
