from time import sleep

def loading(count):
    for i in xrange(count):
        sleep(1)
        print "\n."

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

alone_bearings_final = """
To the south is the office. You wonder how many others are logged in, accessible
and in need of help you could provide by being there and listening.

What do you do?\n"""

alone_bearings_start = """
To the south is the office, which suddenly seems a lot less depressing than it
once did.

What do you do?\n"""

alone_extra_final = """
You feel it would probably be best to leave. There might be others, elsewhere,
who could use your help."""

alone_extra_lose = """
.

.

.

.

.
turn off the projector and stuff please

.

.
i don't really want to talk to anyone"""

alone_extra_proj_off = """
The young lady is in evident distress but is bearing it very quietly. You
have turned off the projector. Maybe its worth looking at?"""

alone_extra_start = """
The young lady is in evident distress but is bearing it very quietly. Maybe it's
also worth taking a look at the projector. Not that it has anything to do with
the lady or her distress. """

alone_extra_win = """
.

.

.

.
thanks for your help

.
theres something under the projector

.

.
i think someone like you could do some good with it"""

def alone_failed():
    loading(1)
    print "hmmm i don't think thats right"
    loading(2)
    print "don't worry about it"

alone_intro = """
The place is horribly unkempt. It smells of sweat, tears, and stale urine. A
young woman is sitting behind a table with a laptop open in front of her. She is
facing away from you. You can tell that she notices that you entered, but she
doesn't move very much. A small, modern projector is to your right. It is
pointing across the room to the wall on your left."""

def alone_hint():
    loading(2)
    print "lol i don't think any of those are it.."
    loading(3)
    print "he says he feels worn out"
    loading(2)
    print "and that hes tired of trampling on others"
    loading(1)

def alone_look_under_final():
    print """
There's nothing else there."""
    sleep(2)

def alone_look_under_solved():
    print """
You crouch down beside the projector and take a look beneath it. There is a
a stone lying there, collecting dust. Perhaps it'd be a good idea to take it?"""
    sleep(4)

def alone_look_under_start():
    print """
You would. But why bother?"""
    sleep(2)

def alone_proj_look_basic():
    print """
There seems to be a wire connecting the projector to the laptop in front of the
lady at the desk."""
    sleep(3)

def alone_proj_look_lid():
    print """
It seems like the projector lid isn't open."""
    sleep(3)

def alone_proj_look_on():
    print """
Upon closer inspection you realize that the projector isn't on."""
    sleep(3)

def alone_proj_look_power():
    print """
Wow, yeah. This projector isn't even plugged in."""
    sleep(2)

def alone_projector_close():
    print """
No sense exposing the lens to unnecessary damage. You pick up the lid and
secure it on top of the projection lens."""
    sleep(2)

def alone_projector_lid():
    print """
You shouldn't have worried about it. The lid was already closed. Simple amazing
how things work out like that."""
    sleep(2)

def alone_projector_no_lid():
    print """
You reach for the lid only to realize that its not there! Where is it?!"""
    sleep(2)
    print """
Right. It's next to the projector where you left it. It probably won't be
necessary to open the lens lid when it is already open. You may rest."""
    sleep(3)

def alone_projector_no_power():
    print """
It doesn't seem like the projector has any power. Is it plugged in?"""
    sleep(2)

def alone_projector_open():
    print """
You go to front of the projector and pop open the cap. You set it down nicely
next to the projector."""
    sleep(3.5)

def alone_projector_powered():
    print """
You had never unplugged the projector. Is that what you want to do?"""
    sleep(2)

def alone_projector_power_off():
    print """
You guess that it's best to unplug the projector so that it doesn't suck any
ghost power. Saving electricty is important, it means less combustible fuel
needs to be burned to produce it... somewhere."""
    sleep(5)

def alone_projector_power_on():
    print """
You walk over to the projector plug, pick it up, and plug it into the wall
socket over on the wall to your right."""
    sleep(3)
    print """
The projector probably has some power now."""
    sleep(2.5)

def alone_projector_running():
    print """
Good news! The projector was already on. Saves you the energy from having to
reach over and press the power button. Congratulations!"""
    sleep(3)

def alone_projector_turn_off():
    print """
If you're not going to use the projector, why waste electricity? Best to power
it off. You do just that and the world feels slightly greener already."""
    sleep(5)

def alone_projector_turn_on():
    print """
The projector fan whirs into life and some blinkies come on. All systems are go."""
    sleep(3)

def alone_projector_unpowered():
    print """
You had never plugged in the projector. You can't double unplug it, that would
be madness."""
    sleep(2)

def alone_projector_was_off():
    print """
You reach to turn the projector off."""
    sleep(2)
    print """
The projector was already off. You self-reflect on whether or not you might just
be a hater."""
    sleep(2)
    print "\nNah."
    sleep(2)

def alone_riddle():
    print """
An image displays on the projector screen on the left side of the room.
Something is loading."""
    sleep(6)
    loading(4)
    print """
An empty text document appears on the screen. Then you hear the soft sounds of
typing on the young lady's keyboard."""
    sleep(6)
    loading(2)
    print "\nhi"
    loading(1)
    print "\nnot sure why your here"
    loading(3)
    print "\nwhat do you want"
    sleep(1.5)
    print "\n" *5
    print """
Before you have a chance to respond she goes on."""
    sleep(1.5)
    loading(3)
    print "k my friend is having some kind of breakdown"
    loading(3)
    print "mby you can help"
    loading(5)
    print "he says he feels like that which has a tongue but cannot taste"
    loading(1)
    print "has a soul but cannot feel"
    loading(2)
    print "what is he talking about??"

def alone_solved():
    loading(5)
    print "yeah"
    loading(1)
    print "he said yeah"
    loading(2)
    print "thank you"
    loading(3)
    print "look under the projector, theres something there you should take"

def alone_talk_to_girl():
    print """
Oh, I'm sorry. Did I mention that there was a girl here?"""
    sleep(3)
    print """
Right, I don't think I did. Why don't you take your patronizing tone out of
here, bud."""
    sleep(3)

def alone_talk_to_lady():
    print """
'Hey,' you say. The lady doesn't move."""
    sleep(2)
    print """
'Are you alright?' Nothing."""
    sleep(2)
    print """
You take the cue. You'd probably have better luck talking to the projector."""
    sleep(3)

def alone_talk_to_projector():
    print """
You see that the projector might be in emotional stress."""
    sleep(3)
    print """
'It's going to okay. You will make it through this,' you tell it."""
    sleep(3)
    print """
Deep down, you feel the projector heard you. It will be okay."""
    sleep(3)

bad_moves = "\nYou can't go there from here.\n"

battlefield_bearings1 = """
The soldier on the ground notices you. She's shaking and beckoning you
to come closer. To the north is the dark tunnel.

What do you do?\n"""

battlefield_bearings2 = """
The soldier lies still. To the north is the dark tunnel.

What do you do?\n"""

battlefield_extra_start = """
Looking around a little wider, the scene is actually not so pitiful!
There are flourishing trees nearby with some birds chirping cheerily.
How fun.

The soldier wants you to talk to her."""

battlefield_extra_win = """
Looking around a little wider, the scene is actually not so pitiful!
There are flourishing trees nearby with some birds chirping cheerily.
How fun.

There is a fairly sizeable stone in the soldier's relaxed right hand,
perhaps it's something worth taking?"""

battlefield_extra_fail = """
Looking around a little wider, the scene is actually not so pitiful!
There are flourishing trees nearby with some birds chirping cheerily.
How fun.

The soldier is certainly in agony. Maybe it is best to leave her alone."""

battlefield_extra_final = """
Looking around a little wider, the scene is actually not so pitiful!
There are flourishing trees nearby with some birds chirping cheerily.
How fun.

The soldier lies peacefully."""

battlefield_failed = """
The soldier stares at your fixedly. Her body becomes rigid. Her left hand
drops and she clutches both hands together.

'Leave me,' she whispers."""

def battlefield_hint():
    print """
The soldier whispers,

'Don't let all my layers whither and die.'"""
    sleep(1)

battlefield_intro = """
After walking south from the dark tunnel you come across a pretty grim scene.
It looks like a soldier had been hit by the bomb or whatever it was that created
this ruin. The soldier is clearly in excrutiating pain and is doing what she can
to stay conscious for as long as possible. It doesn't seem like that will be for
much longer. You might say she's on her last legs. But that would seem a bit
disrespectful as it seems that bomb had dismembered her of exactly those legs
that the phrase seems to be referring to."""

def battlefield_riddle():
    print """
You approach the soldier and she looks you right in the eyes. As you approach
you notice that her eyelids have been torn off in the twisted explosion. She
doesn't appear to ever blink and you feel very uneasy."""
    sleep(5)
    print "\nThe soldier appears to be disoriented. She speaks:"
    sleep(2)
    print """
'You use a knife to slice my head, and weep beside me when I am dead.'"""
    sleep(3)
    print "\n'What am I?'"
    sleep(1.5)

battlefield_solved = """
The soldier appears relieved. Her left hand drops. You can see she the ghost is
passing. You notice that her right hand also relaxes revealing something inside."""

def battlefield_take_soldier():
    print """
You aren't whisking anybody away today, buster."""
    sleep(2)

def battlefield_touch_soldier():
    print """
You decide not to do it at the last moment."""
    sleep(2)

butcher_bearings_after = """
The man regards you as an entity of no greater interest than any of the
displayed pieces of meat below the counter. To the south is the dark tunnel,
maybe it's best to head back and get away from this vaguely uncomfortable place.

What do you do?\n"""

butcher_bearings_final = """
There doesn't appear to be much of particular interest around here. To the south
is the dim tunnel. Go or stay, you feel quite comfortable.

What do you do?\n"""

butcher_bearings_start = """
The man doesn't appear to be terribly busy and there are no other patrons. To
the south is the dark tunnel, which in some ways is more welcoming than this
cold butcher shop.

What do you do?\n"""

butcher_extra_final = """
The man continues to sharpen the knife. He is part of the room. You feel whole."""

butcher_extra_lose = """
The man has gone back to sharpening his knife. He doesn't seem to really be
all that interested in you. Maybe its best to just get out of here and be by
yourself in the dark tunnel. Alone. Like always."""

butcher_extra_start = """
The pig swings invitingly in the back room. There are some cuts of meat lying
about. The butcher glances at you periodically as he is sharpening the knife.
Perhaps you could talk to him?"""

butcher_extra_win = """
After watching you look around nervously, the butcher catches your attention and
indicates a tray at the end of the counter. The tray is labeled 'gratis'. There
are some lumpy looking cuts in there, but also what appears to be a stone. Maybe
the stone could be worth taking?"""

butcher_failed = """
The man gives a cool laugh. Maybe he likes you after all! He gives you a nod.

Suddenly he seems to lose most of his interest in you and goes back to
sharpening the knife."""

def butcher_hint():
    print """
The man laughs a kind-sounding laugh,

'Maybe you 'ought to have a rest,' he says."""
    sleep(1.5)

butcher_intro = """
A fairly standard-looking butcher shop. There is metal counter over a glass
display where certain cuts of meat are shown. A smooth, trim man with glasses
stands behind the counter. He is manually sharpening a knife with a stone. The
knife is not, in fact, a butcher's cleaver. Somehow this fact doesn't give you
any deep sense of comfort. Behind the man you see a skinned pig hanging from a
hook. How quaint."""

def butcher_riddle():
    print """
You look at the man and indicate that you would like his attention. He puts his
knife down firmly, perhaps a tad too firmly, and he walks to the end of his side
of the counter and gives you a fake smile."""
    sleep(3)
    print "\nAfter a few awkward moments, he speaks in a gentle voice:"
    sleep(2)
    print """
'What loses its head in the morning and gets it back at night?'"""
    sleep(3)

butcher_solved = """
The man gives a cool laugh. Maybe he likes you after all! He looks across the
room to the end of the counter and then back at you, giving a nod.

Suddenly he seems to lose most of his interest in you and goes back to
sharpening the knife."""

def butcher_take_meat():
    print """
The butcher sees you reaching for one of the cuts of meat. He clears his throat
to catch you attention and then shakes his head prohibitively.

Maybe it's best to listen to the man with the knives. You leave the cuts alone."""
    sleep(4)

def butcher_take_pig():
    print """
The urge is to take this pig and rescue it from this cold, cold place."""
    sleep(3)
    print """
But after a few seconds of reflection the notion seems a bit silly. You wouldn't
even be able to carry the thing without chopping it up first, and that just
seems counter-intuitive to your whole plan."""
    sleep(4)
    print "\nYou give it up."
    sleep(2)

def butcher_touch_meat():
    print "\nSquishy."
    sleep(2)
    print """
The butcher doesn't seem to like you touching the meat. Probably best to not do
that anymore."""
    sleep(3)

def butcher_touch_pig():
    print """
Yes, the pig really does look like it would enjoy the smooth touch of a caring
human. Unfortunately, it's behind the counter and you don't feel the man
sharpening the knife would appreciate you going back there."""
    sleep(4)

dining_room_bearings_after = """
The dining table stands as eerily as ever. To the east is that tunnel, the one
where your frog buddy is probably still croaking along, might be nice to hear
some of those sweet frog sounds right about now.

What do you do?\n"""

dining_room_bearings_start = """
There are some things on the dining table. To the east is that tunnel, the one
where your frog buddy is probably still croaking along.

What do you do?\n"""

dining_room_bearings_final = """
The dining table is still. To the east is that tunnel with the frog.

What do you do?\n"""

dining_room_extra_fail = """
This place gives you the creeps.

You've scribbled all over the note on the table with no good result."""

dining_room_extra_final = """
You somehow feel at ease in the silence of this room.

The pendulum swings and the curtains dance. You feel you are not unlike them.
The thought give you a sense of ease."""

dining_room_extra_start = """
Something about this place seems off but you feel it's safest to just not
mention it.

There is a note on the table that is perhaps worth reading."""

dining_room_extra_win = """
Yes, this place is definitely unnaturally quiet. The clock moves without a
noise, the curtains dance soundlessly.

By the window you hear a slight tapping, a stone seems to be moving almost
imperceptibly as it is grazed by a silk curtain. Maybe it's worth taking?"""

dining_room_failed = """
For some reason your heart is beating extremely loudly. You feel pretty sick.
Maybe it's best to get out of here?"""

def dining_room_hint():
    print """
There is only one line left,

You start to feel a bit nervous and can hear your heart beating in your chest.
It's really damn quiet in this weird place."""
    sleep(2)

dining_room_intro = """
This room is extremely gaudy. They've got little fountains with little rocks and
fishies. The sofa is upholstered with some fancy fabric that probably costs more
per square foot and the an ordinary 2500 square foot house in the suburbs. They
even got one of the grandfather clocks with the pendulum swinging back and
forth. The window at the back of the dining room is open and the gorgeous silk
curtains are floating lyrically along. You half-expect a wild butler to appear."""

def dining_room_leave_pen():
    print """
You decide to leave the pen here, it seems somehow appropriate."""
    sleep(4.5)

def dining_room_look_outside():
    print """
You see nothing but brightness. Your corneas protests."""
    sleep(2)

def dining_room_no_pen():
    print """
What an interesting question. Well, without a nice pen to respond to the
inquiry it is probably best to just back away. Heck, even a ballpoint pen would
have done the job."""
    sleep(4.5)

def dining_room_quiet():
    print """
You suddenly realize just how quiet this place is. Apart from the noises made by
your body, there does seem to be one other sound in the room."""
    sleep(1.5)

def dining_room_riddle():
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

def dining_room_sit():
    print """
On second thought, your clothes are probably too dirty. Wouldn't want to get
anyone mad for dirtying their million dollar sofa. You decide to keep standing."""
    sleep(4)

def dining_room_take_big():
    print """
It is bigger than you are."""
    sleep(2)

def dining_room_take_curtain():
    print """
You don't feel like being a common criminal."""
    sleep(2)
    print """
Right now."""
    sleep(2)

def dining_room_take_water():
    print """
... And how would you like to do that, exactly?"""
    sleep(2)

def dining_room_touch_clock():
    print """
It's made of some pretty nice wood."""
    sleep(2)

def dining_room_touch_curtain():
    print """
Silk feels nice."""
    sleep(2)

def dining_room_touch_sofa():
    print """
Soft, smooth, and snobby."""
    sleep(2)

def dining_room_touch_water():
    print """
Water feels nice."""
    sleep(2)

def dining_room_yes_pen():
    print """
Hmmm. Good thing you had the foresight to pick up this trusty ballpoint pen."""
    sleep(2)

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

def indentation_hint():
    print """
This stone seems like it might fit into one of those indentations you felt
earlier at that beautiful door."""
    sleep(2.5)

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

def no_bag():
    print """
You don't think you can carry any more of these stones at once. Maybe it makes
sense to drop them off somewhere. Or maybe if you had some kind of container to
carry them in, that would probably make things easier too."""
    sleep(5)

racetrack_bearings_after = """
The robot has gone off to survey the other people. You are out of rocks. To the
west is the office, it seems a lot less crazy than this place.

What do you do?\n"""

racetrack_bearings_final = """
These people are in good hands, you feel. Good, comfortable robot hands. To the
west is that lonesome office, but that's okay, it is only one room.

What do you do?\n"""

racetrack_bearings_start = """
The hugbot and the scared humans are scattered through the track. To the west is
that office, it's looking mighty comfy right about now - no need to deal with
life's problems there!

What do you do?\n"""

racetrack_extra_final = """
You feel loved."""

racetrack_extra_lose = """
There doesn't appear to be anything else that's interesting around here.
Everyone is just sad and mopey."""

racetrack_extra_no_rock = """
A person is cowering a few feet away from you. The robot is directly in front of
you, paying most of its attetion in the opposite direction."""

racetrack_extra_start = """
There is small rock on the ground next to you. A person is cowering a few feet
away from you. The robot is directly in front of you, paying most of its
attention in the opposite direction."""

racetrack_extra_win = """
You see now that the hugbot had just been looking for the person who was most in
need of a hug. Apparentely it calculated that this person was you.

It seems that the robot had dropped some kind of stone. The idea is kind of
gross but the stone looks clean and harmless. Maybe you should take it?"""

racetrack_failed = """
Well, that was a long hug. You're not quite sure why that was necessary. The
robot backs away slightly and its Cheshire cat face 'smiles.'

'Bye-bye for now, sweet friend, others do have need of me.'"""

def racetrack_hint():
    print """
'If I am a spoon in hugging you, the safeword be a different hue,' the hugbot
says."""
    sleep(3)

racetrack_intro = """
This is no ordinary racetrack. You spot some kind of machine - a hugbot on
tanktreads with 'Happy Birthday' written on its back and 'You'll get yours'
written on the front. Its face reminds you of the Cheshire Cat except extremely
tall instead of wide. The eyes pop out of its face and sharply looking around
the track. There are a number of ragged people at the edges of the track,
evidently trying to get as far away from the hugbot as they can. The hugbot
appears to be deciding who to go after next."""

def racetrack_riddle():
    print """
You hurl the rock at the robot. If you had a killer arm you might have actually
gotten it somewhat close to the robot, which is a fair bit further away than you
had judged."""
    sleep(4)
    print """
Luckily (?) the robot seems to have noticed you regardless. It turns around and
whips over to you."""
    sleep(2)
    print """
The robot approaches very quickly and gets menacingly close to you. The exhaust
that oddly appears have been designed to point forward makes it feel like the
Cheshire face sending hot air straight to your face."""
    sleep(4)
    print """
'You look lonesome,' the robot drones. 'Care for a hug?'"""
    sleep(3)
    print """
Before you can respond the robot hugs you. The embrace is tight but not painful.
It's robot arms are made of some kind of impossibly comfortable material.
Something cracks inside and you feel yourself on the verge of tears, but you
restrain yourself. 'This is just a robot!' you think to yourself."""
    sleep(7)
    print """
'Remember you can always say the safeword if you feel you cannot accept the love
that you deserve,' the robot says."""
    sleep(5)
    print """
'Safeword?' you hear yourself ask."""
    sleep(3)
    print """
'Yes, friend,' the robot says.

'I have a few points, but we're not competing, and I'll help you win when you
are eating. What I am, the safeword be.'"""
    sleep(4)

def racetrack_solved():
    print """
The hugbot backs away suddenly.

'If you feel you don't need my acceptance I can only hope it is because you have
dear friends of your own,' it says."""
    sleep(5)
    print """
'I will leave this here, if you choose to pick it up, may be a reminder for you
of what is essential for happiness.'

You hear something drop on the other side of the robot. The robot then drives
away, presumably to give some robot loving to these other humans."""

def racetrack_talk():
    print "Who would you like to talk to, exactly?"
    sleep(2)

def racetrack_take_rock():
    print """
You pick up the rock. Hefty."""
    sleep(3)

def racetrack_talk_to_robot():
    print """
Talk to the robot? What is your problem? That is a machine bent on killing
people foolish enough to try reasoning with it! No way! Why don't you go try
talking to a wall or something."""
    sleep(4)

def racetrack_talk_to_human():
    print """
You approach the person with the intention to speak with him."""
    sleep(3)
    print """
'Hello,' you say."""
    sleep(4)
    print """
A fit of loud sobbing comes over the person. Maybe its best just to leave him
alone."""
    sleep(4)

def racetrack_throw_rock():
    print """
Uh. This is kind of the only rock you see around. So maybe you should think
about where the best place to throw it might be."""
    sleep(3)

def racetrack_throw_rock_at_human():
    print """
In a fit of wickedness you throw a rock at the cowering human. You feel
deviously sinister as you let go of the rock."""
    sleep(4)
    print """
BAM! It's like you've been throwing stones at defenceless cowering humans all
your life."""
    sleep(5)
    print """
The person seems to be legitimately knocked out and potentially bleeding. Wow."""
    sleep(5)
    print """
Suddently the hugbot spins around and seems to notice you. The other cowering
humans are also taking note of you, the rock slinging bad-ass."""
    sleep(5)
    print """
Oh god! Everyone starts running at full speed to get you. The hugbot's 'You'll
get yours' sign is particularly sinister as it approaches at such a high speed."""
    sleep(6)
    print """
You quickly back up out of the racetrack and lock the door behind you. That was
pretty convenient. Probably best if you don't try going back in there anymore.\n"""
    sleep(3)
    raw_input("Press ENTER to escape. > ")

def racetrack_touch_rock():
    print """
Good thing that you tried to touch that rock before taking it. Now you can
confirm without a doubt that it is a rock."""
    sleep(3)

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
    print "\nHmmm, it seems like all the networks are passworded."
    sleep(4)
    print "\nAfter failing with some predictable guesses, you decide it is hopeless."
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

def stone_of_compassion_pickup():
    print"""
You pick up the stone. It is a bit dusty. But once your brush it off gently you
notice that the stone is as brilliant as any you have ever looked on. Looking at
the stone, you see the word 'COMPASSION' written on it."""
    sleep(5)

def stone_of_friendship_pickup():
    print"""
You pick up the stone. It is warm to the touch. It probably had that hugbot's
exhaust blowing on it too. Somehow this stone reminds you of some of the
happiest times you've had with some close friends, along ago. Looking at the
stone, you see the word 'FRIENDSHIP' written on it."""
    sleep(5)

def stone_of_peace_pickup():
    print"""
You pick up the stone. The man doesn't seem to notice at all. Somehow that's
okay. You wonder why he seemed to exact such an influence on you. You feel more
connected to yourself. Looking at the stone, you see the word 'PEACE' written
on it."""
    sleep(5)

def stone_of_practice_pickup():
    print"""
You pick up the stone. You feel more sure of yourself. There is much that you
do not know, but there is much that can be seen, experienced and learned. On the
stone you see the word 'PRACTICE'."""
    sleep(5)

def stone_of_respect_pickup():
    print"""
You pick up the stone. Perhaps you are imagining this, but you feel the soldier
wouldn't mind for you to take this. On the stone you see the word 'RESPECT'."""
    sleep(5)

def stone_of_silence_pickup():
    print"""
You pick up the stone. The room is now entirely quiet. Somehow, even your own
body has seeemed to slow down and ease into the silence of this room. You feel
well. On the stone you see the word 'SILENCE'."""
    sleep(5)

talking = ["'Yes, I am talking'", "'I know English.'", "'Words words words.'",
            "'Can I stop talking now?'",
            "'Am I supposed to say anything in particular?'", "'La la la.'",
            "'The power of human expression is being tapped into right now.'",
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

world_bearings_start = """
To the north is the strangely incongruous passage that leads back to the office
from which you came.

What do you do?\n"""

def world_chill_final():
    print "\nYou feel you could do more good if you did not."
    sleep(2)

def world_chill_start():
    print """
It is pretty comfortable."""
    sleep(3)
    print "\nYou wonder what else you can see if you go walk around a bit."
    sleep(2)
    print "\nYou get up."
    sleep(2)

def world_enjoy_final():
    print "\nThe world is rich."
    sleep(2)

def world_enjoy_start():
    print """
Simply breathtaking..."""
    sleep(6)
    print "\nYou wonder if some of the computers in the office have cable internet."
    sleep(2)
    print "\nYou're not really paying much attention any more."
    sleep(2)

world_extra_lose = """
Where the elephant was there is now nothing. To your left is a sizable rock.
There is an amazing view to enjoy and many mountains to look at. It is very hot."""

world_extra_start = """
There is an elephant sitting cross-legged in front of you. To your left is a
sizable rock. There is an amazing view to enjoy and many mountains to look at.
It is very hot."""

world_extra_win = """
In front of you is a stone lying on the ground. Perhaps the stone is worth
picking up. To your left is a sizable rock. There is an amazing view to enjoy
and many mountains to look at. It is very hot."""

def world_fan_final():
    print "\nAs hot as it is, you know that you will survive."
    sleep(3)

def world_fan_start():
    print """
The effect is not worth the effort"""
    sleep(2)

world_failed = """
You blink and the elephant is gone. There is no trace of it."""

def world_gaze_final():
    print "\nYou see the mountains."
    sleep(2)

def world_gaze_start():
    print """
You feel tiny."""
    sleep(3)
    print "\nYou wonder how easy it would be to climb up one of those mountaints."
    sleep(2)
    print "\nYou'll do it someday."
    sleep(2)

world_intro_final = """
Incredible. This passage somehow led to the top of a mountain. The view in
better than any you have ever experienced. You feel miniscule. The mountains
speak of something out of The Cossacks by Tolstoy. The palette has oranges, deep
greens, light blues and everything in between mixed in."""

world_intro_start = """
Incredible. This passage somehow led to the top of a mountain. The view is
better than any you have ever experienced. You feel miniscule. The mountains
speak of something out of The Cossacks by Tolstoy. The palette has oranges, deep
greens, light blues and everything in between mixed in. Perhaps more striking
is the tiny (relatively speaking) elephant sitting cross-legged in loose
clothing. The elephant is facing you, but its eyes do not open as you enter."""

def world_meditate_final():
    print "\nThere is much to do."
    sleep(2)

def world_meditate_start():
    print """
You sit on the ground and cross your legs."""
    sleep(4.5)
    print "\nYour right leg starts to cramp up."
    sleep(3)
    print "\nYou get up."
    sleep(2)

world_overheating1 = "\nYou feel sweat building up on your brow."

world_overheating2 = "\nYou're starting to sweat through your clothing"

world_overheating3 = "\nYou starting to feel like you're swimming in your clothes."

world_overheating4 = "\nThe heat is becoming oppressive."

world_overheating5 = "\nYou feel close to passing out."

world_overheating6 = "\nYou feel nauseous."

def world_riddle():
    print "\n'Hello,' you say."
    sleep(3)
    print "\nThe elephant opens its eyes."
    sleep(2)
    print """
'I am heavy but not backwards,' it intones."""
    sleep(3)
    print """
'What am I?'"""
    sleep(2)
    print "\nYou feel compelled to answer."
    sleep(1.5)

def world_rock_final():
    print "\nIt feels as it should."
    sleep(2)

def world_rock_start():
    print "\nJust another rock."
    sleep(2)

def world_rock_buddy_final():
    print "\nWords would do no good."
    sleep(3)

def world_rock_buddy_start():
    print """
'How are you doing, rock?' you say."""
    sleep(3)
    print "\nOk..."
    sleep(1.5)

def world_sit_final():
    print "\nNot right now."
    sleep(2)

def world_sit_start():
    print """
The ground is very hot from the sun."""
    sleep(3)
    print "\nThis sucks."
    sleep(2)
    print "\nYou get up."
    sleep(2)

world_solved = """
You blink and the elephant is gone. It seems like there is hardly a trace of it.
There is some small object where it elephant appeared to be."""

def world_touch():
    print "\nSeems like a bad idea."
    sleep(2)
