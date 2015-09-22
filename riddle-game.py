from sys import exit
#from time import sleep
from fakesleep import sleep

line_break = "--------------------------------"

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

    def stones_carried(self):
        count = 0
        for item in self.items:
            if item.split()[0] == "Stone":
                count += 1
        return count

class Room(object):

    guesses_left = 5
    solved = False
    stone_here = False
    visited = False
    valid = ['help', 'walk', 'walk north', 'walk south', 'walk east', 'walk west',
            'go', 'go north', 'go south', 'go east', 'go west', 'inventory',
            'inv', 'intro', 'look around', 'look', 'take']
    vague_moves = ['walk', 'go', 'take']
    bad_moves = []
    good_moves = []
    extra = ""
    helper ="""
Here are some actions that you can take:

- walk (somewhere)
- inventory (or inv)
- look around (or look)
- intro
- touch (something)
- take (something)
- place (something)
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
            if action == 'touch stone' and 'take stone' in self.good_moves:
                print "\nHard.\n"
            elif action not in self.valid and action not in self.good_moves:
                print "\nI'm sorry, but you can't %r.\n" % action
            if action in self.bad_moves:
                print "\nYou can't go there from here.\n"
            if action in self.vague_moves:
                print "\nCommunication is important. Please be more specific!\n"
            if action == 'help':
                print line_break
                print "\n" * 6
                print self.helper
            if action == 'look around' or action == 'look':
                print line_break
                print "\n" * 8
                print self.extra
                print self.bearings
            if action == "intro":
                print line_break
                print "\n" * 6
                print self.intro
                print self.bearings
            if action == "inventory" or action == "inv":
                print line_break
                print "\n" * 4
                inv.show()
                print "\nWhat do you do? \n"
        print "\nYou attempt to %s." % action
        sleep(0)
        return action

    def stone_available(self):
        if self.stone_here and self.solved and "take stone" not in self.good_moves:
            self.good_moves.append("take stone")
        else:
            pass

class StartingRoom(Room):

    start_of_game = True
    good_moves = ['go north', 'walk north', 'take pen']
    bad_moves = ['walk south', 'walk east', 'walk west', 'go south', 'go east',
                'go west']
    wake_up = """You wake up.

Your mind is foggy but slowly you get your bearings.

You are in a blue-tinted room surrounded by what seems to be drywall. You are
lying on a mattress sprawled in the middle of the room. You're dressed normally.
Nothing seems to have gone wrong but you don't have a clear idea of where you
are or why."""
    extra = """
This looks like the sloppy apartment of a bachelor. How lovely.

There appears to be a pen on the floor near to the mattress."""
    intro = """
This is the room you woke up in. Apart from the spartan set up and the random
mattress placement, it's not so bad."""
    bearings = """
There is some junk lying around. There is a hallway to the north.

What do you do?\n"""

    def enter(self):
        if self.start_of_game == True:
            print self.wake_up
            self.start_of_game = False
        print self.bearings
        action = self.action()
        if action == "go north" or action == "walk north":
            return "middle"
        if action == "take pen":
            print """
You pick up the pen. It is a blue ballpoint. Can never have enough pens."""
            self.good_moves.remove("take pen")
            inv.items.append("ballpoint pen")
            sleep(3)
            self.extra = """
This looks like the sloppy apartment of a bachelor. How lovely.

The rest of the junk on the floor is junk."""
            return self.enter()

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
    extra = """
The smell of singed hair and old rubber is not exactly comforting."""
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
This door is incredible. It is probably the best door you have ever seen.
Picture the nicest door you ever saw. That's what this looks like. It has three
indentations to either side of it."""
    extra = """
There is a bag made out of fabric on the floor next to the door. It is seriously
messing up how cool this door looks.

The door looks so beautiful that you would love to touch it, not that you'd
expect to learn anything. There are also some slightly more useful looking
indentations that are within reach."""
    bearings = """
An immaculate door is just to the north of you. Behind you, to the south, is the
big, dripping room.

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
            TheDoor.touched_indentations = True
            print "\nThese indentations are cold."
            sleep(2)
            have_stone = False
            for stone in self.stones.keys():
                if stone in inv.items:
                    have_stone = True
            if have_stone:
                print """
It seems like you could place some of these stones into some of these
indentations."""
                sleep(3.5)
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
You take The %s and place it the indentation where it fits best.""" % stone
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
                    self.bearings = """
The immaculate door is open! Beyond it, to the north, is one of those weird
foggy screens that you can't see behind but can probably walk through without
getting terribly hurt. Behind you, to the south, is the big, dripping room.

What do you do?\n"""
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
                    self.bearings = """
The immaculate door is open! Beyond it, to the north, is one of those weird
foggy screens that you can't see behind but can probably walk through without
getting terribly hurt. Behind you, to the south, is the big, dripping room.

What do you do?\n"""
                    return self.enter()
            else:
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
                self.attempted_door = True
                sleep (1.5)
                return self.enter()

        if action == 'go north' or action == 'walk north':
            if self.door_open:
                return 'end'
            else:
                print "\n'Believe,' you whisper to yourself and march toward the door."
                sleep(3)
                print "\n'Ouch!'"
                sleep(2.5)
                print """
Yes, this door really is there. Maybe it's worth trying to open it before
attempting to channel Houdini some more."""
                sleep(3.5)
                return self.enter()

    def stone_count(self):
        count = 0
        for stone in self.stones.keys():
            if self.stones[stone]:
                count += 1
        return count

class Left(Room):

    good_moves = ['go east', 'walk east', 'walk south', 'walk east',
                    'walk west', 'go south', 'go east', 'go west', 'go north',
                    'walk north']
    bad_moves = []
    intro = """
After walking through the dark tunnel for a while you begin to feel quite
certain of one thing: it is very dark here. Not that that's a problem or
anything. Though if it wasn't for the faint glimmers of other places peaking
through in the distance you would probably begin to lose your mind right now
about. Hey, maybe you'll be doing that regardless, why not!"""
    extra = """
The sounds made by a croaking frog are somehow comforting. Why it is here, you
do not ask, only that you are not alone and perhaps the world is not as scary
a place as you once thought it was."""
    bearings = """
To the north appears to be a butcher shop. To the west you see the glimmer of a
upperclass dining room, complete with fine china and ornamental lamps. The the
south are some sort of ruins, seemingly made by a bomb explosion. To the east is
the dumpy, drippy room.

What do you do?\n"""
    def enter(self):
        if self.visited == False:
            print self.intro
        self.visited = True
        print self.bearings
        action = self.action()
        if action == "go south" or action == "walk south":
            return "battlefield"
        if action == "go east" or action == "walk east":
            return "middle"
        if action == "go west" or action == "walk west":
            return "dining room"
        if action == "go north" or action == "walk north":
            return "butcher"

class Right(Room):

    good_moves = ['go east', 'walk east', 'walk south', 'walk east',
                    'walk west', 'go south', 'go east', 'go west', 'go north',
                    'walk north', 'touch computer', 'touch computers']
    bad_moves = []
    intro = """
Wow. A totally intact office. There are even a bunch of computers, some of
which are just idling. As you walk by desktops and laptops you feel a growing
lack of fulfillment. The desire to throw the computers across the room and dance
in the wreakage grows stronger and stronger. But no. You mustn't. You love
technology. You need it. You feel certain of this. You begin to let go.
Surrender. Everything will be okay."""
    extra = """
There are a bunch of computers that you wouldn't mind touching. The sounds of
computer fans are oddly calming. """
    bearings = """
To the north appears to be another bachelor's apartment. You wonder what the
rent is around this place. To the east seems to be the entryway to a racetrack.
The south is an opening leading to the top of a mountain. Whoa. To the west is
that large sack of moist newspapers that might be called a great hall.

What do you do?\n"""
    def enter(self):
        if self.visited == False:
            print self.intro
        self.visited = True
        print self.bearings
        action = self.action()
        if action == "go south" or action == "walk south":
            return "world"
        if action == "go east" or action == "walk east":
            return "racetrack"
        if action == "go west" or action == "walk west":
            return "middle"
        if action == "go north" or action == "walk north":
            return "alone"
        if action == "touch computer" or action == "touch computers":
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
            return self.enter()

class Battlefield(Room):

    stone_here = True
    good_moves = ['go north', 'walk north', 'talk to soldier', 'talk',
                'talk to her']
    bad_moves = ['go east', 'walk east', 'walk south', 'walk west',
                'go south', 'go west', ]
    intro = """
After walking south from the dark tunnel you come across a pretty grim scene.
It looks like a soldier had been hit by the bomb or whatever it was that created
this ruin. The soldier is clearly in excrutiating pain and is doing what she can
to stay conscious for as long as possible. It doesn't seem like that will be for
much longer. You might say she's on her last legs. But that would seem a bit
disrespectful as it seems that bomb had dismembered her of exactly those legs
that the phrase seems to be referring to."""
    extra = """
Looking around a little wider, the scene is actually not so pitiful! There are
flourishing trees nearby with some birds chirping cheerily. How fun.

The soldier wants you to talk to her."""
    bearings = """
The soldier on the ground notices you. She's shaking and beckoning you to come
closer. To the north is the dark tunnel.

What do you do?\n"""
    def enter(self):
        if self.visited == False:
            print self.intro
        self.visited = True
        print self.bearings
        action = self.action()
        if action == "go north" or action == "walk north":
            return "left"

        if (action == "talk" or action == "talk to soldier" or
            action == "talk to her"):
            print """
You approach the soldier and she looks you right in the eyes. As you approach
you notice that her eyelids have been torn off in the twisted explosion. She
doesn't appear to ever blink and you feel very uneasy."""
            sleep(5)
            print "\nThe soldier appears to be disoriented. She speaks"
            sleep(2)
            print """
'You use a knife to slice my head, and weep beside me when I am dead.'"""
            sleep(3)
            print "\n'What am I?'"
            sleep(1.5)
            solution = ""
            while self.guesses_left > 0 and not self.solved:
                print """
The soldier holds up her left hand, with %d digits up.""" % self.guesses_left
                self.guesses_left -= 1
                solution = raw_input("\nHow do you answer? > ").lower()
                if solution == "onion" or solution == "an onion":
                    self.solved = True
                if self.guesses_left == 1:
                    print """
The soldier whispers,

'Don't let all my layers whither and die.'"""
            self.bearings = """
The soldier lies still. To the north is the dark tunnel.

What do you do?\n"""
            if self.solved:
                self.extra = """
Looking around a little wider, the scene is actually not so pitiful! There are
flourishing trees nearby with some birds chirping cheerily. How fun.

There is a fairly sizeable stone in the soldier's relaxed right hand, perhaps
it's something worth taking?"""
                self.stone_available()
                print """
The soldier appears relieved. Her left hand drops. You can see she the ghost is
passing. You notice that her right hand also relaxes revealing something inside."""
            else:
                self.extra = """
Looking around a little wider, the scene is actually not so pitiful! There are
flourishing trees nearby with some birds chirping cheerily. How fun.

The soldier is certainly in agony. Maybe it is best to leave her alone."""
                print """
The soldier stares at your fixedly. Her body becomes rigid. Her left hand drops
and she clutches both hands together.

'Leave me,' she whispers."""
            self.good_moves.remove("talk")
            self.good_moves.remove("talk to her")
            self.good_moves.remove("talk to soldier")
            sleep(4.5)
            return self.enter()

        if action == "take stone":

            if inv.stones_carried() >= 1 and "dirty bag" not in inv.items:
                print """
You don't think you can carry any more of these stones at once. Maybe it makes
sense to drop them off somewhere. Or maybe if you had some kind of container to
carry them in, that would probably make things easier too."""
                sleep(5)
                return self.enter()

            if inv.stones_carried() == 0 or "dirty bag" in inv.items:
                self.stone_here == False
                inv.items.append("Stone of Respect")
                self.good_moves.remove("take stone")
                print"""
You pick up the stone. Perhaps you are imagining this, but you feel the soldier
wouldn't mind for you to take this. On the stone you see the word 'RESPECT'."""
                sleep(5)
                if TheDoor.touched_indentations:
                    print """
This stone seems like it might fit into one of those indentations you felt
earlier at that beautiful door."""
                    sleep(4)
                self.extra = """
Looking around a little wider, the scene is actually not so pitiful! There are
flourishing trees nearby with some birds chirping cheerily. How fun.

The soldier lies peacefully."""
                return self.enter()

class DiningRoom(Room):

    stone_here = True
    good_moves = ['go east', 'walk east', 'read note']
    bad_moves = ['go north', 'walk north', 'walk south', 'walk west',
                'go south', 'go west' ]
    intro = """
This room is extremely gaudy. They've got little fountains with little rocks and
fishies. The sofa is upholstered with some fancy fabric that probably costs more
per square foot and the an ordinary 2500 square foot house in the suburbs. They
even got one of the grandfather clocks with the pendulum swinging back and
forth. The window at the back of the dining room is open and the gorgeous silk
curtains are floating lyrically along. You half-expect a wild butler to appear."""
    extra = """
Something about this place seems off but you feel it's safest to just not
mention it.

There is a note on the table that is perhaps worth reading."""
    bearings = """
There are some things on the dining table. To the east is that tunnel, the one
where your frog buddy is probably still croaking along.

What do you do?\n"""
    def enter(self):
        if self.visited == False:
            print self.intro
        self.visited = True
        print self.bearings
        action = self.action()
        if action == "go east" or action == "walk east":
            return "left"

        if action == "read note":
            print """
You walk over to the table and take a look at the note. The script it's written
in is exquisite. It reminds you of what you imagined Lev Nikolayevich Myshkin's
calligraphy would look like. But then you realize that you had never read The
Idiot, and just heard that one pretentious gentlemen mention it once. You
applaud your selective memory."""
            sleep(5)
            print "\nThe note has only a short phrase written on it:"
            sleep(2)
            print """
'What is so delicate that even mentioning it breaks it?'"""
            sleep(3)
            if "ballpoint pen" not in inv.items:
                print """
What an interesting question. Well, without a nice pen to respond to the
inquiry it is probably best to just back away. Heck, even a ballpoint pen would
have done the job."""
                sleep(4.5)
                return self.enter()
            elif "ballpoint pen" in inv.items:
                print """
Hmmm. Good thing you had the foresight to pick up this trusty ballpoint pen."""
                sleep(2)
                solution = ""
                while self.guesses_left > 0 and not self.solved:
                    print """
Below the note there are still %d lines that are not used up.""" % self.guesses_left
                    self.guesses_left -= 1
                    solution = raw_input("\nWhat do you write? > ").lower()
                    if solution == "silence":
                        self.solved = True
                    if self.guesses_left == 1:
                        print """
There is only one line left,

You start to feel a bit nervous and can hear your heart beating in your chest.
It's really damn quiet in this weird place."""
            self.bearings = """
The dining table stands as eerily as ever. To the east is that tunnel, the one
where your frog buddy is probably still croaking along, might be nice to hear
some of that sweet frog sound right about now.

What do you do?\n"""
            if self.solved:
                self.extra = """
Yes, this place is definitely unnaturally quiet. The clock moves without a
noise, the curtains dance soundlessly.

By the window you hear a slight tapping, a stone seems to be moving almost
imperceptibly as it is grazed by a silk curtain. Maybe it's worth taking?"""
                self.stone_available()
                print """
You suddenly realize just how quiet this place is. Apart from the noises made by
your body, there does seem to be one other sound in the room."""
            else:
                self.extra = """
This place gives you the creeps.

You've scribbled all over the note on the table with no good result."""
                print """
For some reason your heart is beating extremely loudly. You feel pretty sick.
Maybe it's best to get out of here?"""
            print """
You decide to leave the pen here, it seems somehow appropriate."""
            inv.remove("ballpoint pen")
            self.good_moves.remove("read note")
            sleep(4.5)
            return self.enter()

        if action == "take stone":

            if inv.stones_carried() >= 1 and "dirty bag" not in inv.items:
                print """
You don't think you can carry any more of these stones at once. Maybe it makes
sense to drop them off somewhere. Or maybe if you had some kind of container to
carry them in, that would probably make things easier too."""
                sleep(5)
                return self.enter()

            if inv.stones_carried() == 0 or "dirty bag" in inv.items:
                self.stone_here == False
                inv.items.append("Stone of Silence")
                self.good_moves.remove("take stone")
                print"""
You pick up the stone. The room is now entirely quiet. Somehow, even your own
body has seeemed to slow down and ease into the silence of this room. You feel
well. On the stone you see the word 'SILENCE'."""
                sleep(5)
                if TheDoor.touched_indentations:
                    print """
This stone seems like it might fit into one of those indentations you felt
earlier at that beautiful door."""
                    sleep(4)
                self.extra = """
You somehow feel at ease in the silence of this room.

The pendulum swings and the curtains dance. You feel you are not unlike them.
The thought give you a sense of ease."""
                self.bearings = """
The dining table is still. To the east is that tunnel with the frog.

What do you do?\n"""
                return self.enter()

class Butcher(Room):

    stone_here = True
    good_moves = ['go south', 'walk south', 'talk to butcher', 'talk',
                    'talk to man', 'talk to him', 'touch pig', 'take meat',
                    'take cut', 'take pig', 'touch meat', 'touch cut',
                    'take cuts', 'touch cuts', 'talk to the man']
    bad_moves = ['go north', 'walk north', 'walk east', 'walk west', 'go east',
                'go west']
    intro = """
A fairly standard-looking butcher shop. There is metal counter over a glass
display where certain cuts of meat are shown. A smooth, trim man with glasses
stands behind the counter. He is manually sharpening a knife with a stone. The
knife is not, in fact, a butcher's cleaver. Somehow this fact doesn't give you
any deep sense of comfort. Behind the man you see a skinned pig hanging from a
hook. How quaint."""
    extra = """
The pig swings invitingly in the back room. There are some cuts of meat lying
about. The butcher glances at you periodically as he is sharpening the knife.
Perhaps you could talk to him?"""
    bearings = """
The man doesn't appear to be terribly busy and there are no other patrons. To
the south is the dark tunnel, which in some ways is more welcoming than this
cold butcher shop.

What do you do?\n"""
    def enter(self):
        if self.visited == False:
            print self.intro
        self.visited = True
        print self.bearings
        action = self.action()
        if action == "go south" or action == "walk south":
            return "left"

        if action == "touch pig":
            print """
Yes, the pig really does look like it would enjoy the smooth touch of a caring
human. Unfortunately, it's behind the counter and you don't feel the man
sharpening the knife would appreciate you going back there."""
            sleep(4)
            return self.enter()

        if (action == "touch cut" or action == "touch meat" or
            action == "touch cuts"):
            print "\nSquishy."
            sleep(3)
            print """
The butcher doesn't seem to like you touching the meat. Probably best to not do
that anymore."""
            self.good_moves.remove("touch cut")
            self.good_moves.remove("touch cuts")
            self.good_moves.remove("touch meat")
            return self.enter()

        if action == "take pig":
            print """
The urge is to take this pig and rescue it from this cold, cold place."""
            sleep(3)
            print """
But after a few seconds of reflection the notion seems a bit silly. You wouldn't
even be able to carry the thing without chopping it up first, and that just
seems counter-intuitive to your whole plan."""
            sleep(4)
            print "\nYou give it up."
            self.good_moves.remove("take pig")
            sleep(2)
            return self.enter()

        if (action == "take meat" or action == "take cut" or
            action == "take cuts"):
            print """
The butcher sees you reaching for one of the cuts of meat. He clears his throat
to catch you attention and then shakes his head prohibitively.

Maybe it's best to listen to the man with the knives. You leave the cuts alone."""
            self.good_moves.remove("take cut")
            self.good_moves.remove("take meat")
            self.good_moves.remove("take cuts")
            sleep(4.5)
            return self.enter()

        if (action == "talk" or action == "talk to man" or
            action == "talk to butcher" or action == "talk to him" or
            action == "talk to the man"):
            print """
You look at the man and indicate that you would like his attention. He puts his
knife down firmly, perhaps a tad too firlmy, and he walks to the end of his side
of the counter and gives you a fake smile."""
            sleep(3)
            print "\nAfter a few awkward moments, he speaks in a gentle voice:"
            sleep(2)
            print """
'What loses its head in the morning and gets it back at night?'"""
            sleep(3)
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
                solution = raw_input("\nHow do you answer? > ").lower()
                if solution == "pillow" or solution == "a pillow":
                    self.solved = True
                if self.guesses_left == 1:
                    print """
The man laughs a kind-sounding laugh,

'Maybe you 'ought to have a rest,' he says."""
            self.bearings = """
The man regards you as an entity of no greater interest than any of the
displayed pieces of meat below the counter. To the south is the dark tunnel,
maybe it's best to head back and get away from this vaguely uncomfortable place.

What do you do?\n"""
            if self.solved:
                self.extra = """
After watching you look around nervously, the butcher catches your attention and
indicates a tray at the end of the counter. The tray is labeled 'gratis'. There
are some lumpy looking cuts in there, but also what appears to be a stone. Maybe
the stone could be worth taking?"""
                self.stone_available()
                print """
The man gives a cool laugh. Maybe he likes you after all! He looks across the
room to the end of the counter and then back at you, giving a nod.

Suddenly he seems to lose most of his interest in you and goes back to
sharpening the knife."""
            else:
                self.extra = """
The man has gone back to sharpening his knife. He doesn't seem to really be
all that interested in you. Maybe its best to just get out of here and be by
yourself in the dark tunnel. Alone. Like always."""
                print """
The man gives a cool laugh. Maybe he likes you after all! He gives you a nod.

Suddenly he seems to lose most of his interest in you and goes back to
sharpening the knife."""
            self.good_moves.remove("talk")
            self.good_moves.remove("talk to him")
            self.good_moves.remove("talk to butcher")
            self.good_moves.remove("talk to man")
            self.good_moves.remove("talk to the man")
            sleep(4.5)
            return self.enter()

        if action == "take stone":

            if inv.stones_carried() >= 1 and "dirty bag" not in inv.items:
                print """
You don't think you can carry any more of these stones at once. Maybe it makes
sense to drop them off somewhere. Or maybe if you had some kind of container to
carry them in, that would probably make things easier too."""
                sleep(5)
                return self.enter()

            if inv.stones_carried() == 0 or "dirty bag" in inv.items:
                self.stone_here == False
                inv.items.append("Stone of Peace")
                self.good_moves.remove("take stone")
                print"""
You pick up the stone. The man doesn't seem to notice at all. Somehow that's
okay. You wonder why he seemed to exact such an influence on you. You feel more
connected to yourself. Looking at the stone, you see the word 'PEACE' written
on it."""
                sleep(5)
                if TheDoor.touched_indentations:
                    print """
This stone seems like it might fit into one of those indentations you felt
earlier at that beautiful door."""
                    sleep(3)
                self.extra = """
The man continues to sharpen the knife. He is part of the room. You feel whole."""
                self.bearings = """
There doesn't appear to be much of particular interest around here. To the south
is the dim tunnel. Go or stay, you feel quite comfortable.

What do you do?\n"""
                return self.enter()

class Racetrack(Room):
    pass

class Alone(Room):
    pass

class World(Room):
    pass

class End(Room):

    def enter(self):
        print """
This is the end, the room doesn't exist yet, the programmer hasn't coded it yet."""

class Map(object):

    rooms = {'start': StartingRoom(), 'middle': MiddleRoom(), 'door': TheDoor(),
            'left': Left(), 'right': Right(), 'butcher': Butcher(),
            'dining room': DiningRoom(), 'battlefield': Battlefield(),
            'racetrack': Racetrack(), 'alone': Alone(), 'world': World()}

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
# TODO: Add the puzzle rooms
# TODO: Flush out the end room
# TODO: Work out what happens with the soldier and how you get the stone and also
# add the touched_indentations advantage for when the stone is actually picked up
# TODO: Get rid of string literals
# TODO: Make it so take stone after a stone has been taken give a more
# appropriate response
# TODO: Make it so you need the bag to carry more than 1 stone around
# TODO: Make sure "real" sleep is turned on
# TODO: Define certains actions like wait
# TODO: Add sense of ease when you get the Silence stone, making you not want
# to flip comptuters over.
# TODO: Have a counter that checks how many puzzles were failed. If 3 are
# failed, make the game fail in despair.
# TODO: Make the dirty bag appear the first item in the inventory (append it to
# the beginning of the items list)
