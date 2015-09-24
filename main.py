import all_strings
import riddle_game

class Menu(object):

    menu_options = ["1. New", "2. Load"]
    ingame_menu_options = ["1. New", "2. Save", "3. Load", "4. Continue"]
    menu = {1: ["Start a New Game", "new"], 2: ["Load Game", "load"]}
    ingame_menu = {1: ["Start a New Game", "pam"], 2: ["Save Game", "bam"],
                    3: ["Load Game", "uncle sam"],
                    4: ["Continue Game", "roger roger"]}

    def run(self, version):
        if version == 1:
            self.print_menu(1)
            confirmed = False
            while not confirmed:
                try:
                    num = int(raw_input("\nUse a number to pick > "))
                except ValueError:
                    continue
                if num not in range(1, 3):
                    continue
                print "Are you sure you want to %s?" % self.menu[num][0]
                confirm = raw_input("Type 'yes' to confirm > ")
                if confirm.lower() == 'yes':
                    confirmed = True
            return self.menu[num][1]
        if version == 2:
            self.print_menu(2)
            confirmed = False
            while not confirmed:
                try:
                    num = int(raw_input("\nUse a number to pick > "))
                except ValueError:
                    continue
                if num not in range(1, 5):
                    continue
                print "Are you sure you want to %s?" % self.ingame_menu[num][0]
                confirm = raw_input("Type 'yes' to confirm > ")
                if confirm.lower() == 'yes':
                    confirmed = True
            return self.ingame_menu[num][1]

    def print_menu(self, version):
        if version == 1:
            for option in self.menu_options:
                print option
        if version == 2:
            for option in self.ingame_menu_options:
                print option

class SavedGame(object):

    def __init__(self):
        self.items = []
        self.failed_puzzles = 0
        self.starting = ""
        self.rooms = {"start":
                                {'pen': True, 'visited': True,
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
                                'bearings': all_strings.world_bearings_start}}


class FakeGame(object):

    items = []
    failed_puzzles = 0
    starting = "start"
    rooms = {"start":
                            {'pen': True, 'visited': True,
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
                            'bearings': all_strings.world_bearings_start}
                    }


class Cache(object):

    saved_games = []

if __name__ == "__main__":
    tester = Menu()
    tester.run(2)
