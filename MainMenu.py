import all_strings

class MainMenu(object):

    options = {"New Game": pass, "Save Game": pass, "Load Game": pass}

    def run(self):
        pass

class SavedGame(object):

    items = []
    failed_puzzles = 0
    room_by_room = {"starting":
                            {'current': False, 'start': False, 'pen': True,
                            'intro': all_strings.starting_room_intro,
                            'extra': all_strings.starting_room_extra1,
                            'bearings': all_strings.starting_room_bearings1},
                    "middle":
                            {'current': False,
                            'intro': all_strings.middle_room_intro,
                            'extra': all_strings.middle_room_extra,
                            'bearings': all_strings.middle_room_bearings},
                    "door":
                            {'current': False, 'door_open': False,
                            'attempted_door': False,
                            'touched_indentations': False, 'bag here': True,
                            'intro': all_strings.the_door_intro,
                            'extra': all_strings.the_door_extra1,
                            'bearings': all_strings.the_door_bearings1,
                            'Stone of Peace': False, 'Stone of Silence': False,
                            'Stone of Respect': False,
                            'Stone of Practice': False,
                            'Stone of Friendship': False,
                            'Stone of Compassion': False},
                    "left":
                            {'current': False,
                            'intro': all_strings.left_intro,
                            'extra': all_strings.left_extra,
                            'bearings': all_strings.left_bearing},
                    "right":
                            {'current': False, 'racetrack open': True,
                            'intro': all_strings.right_intro,
                            'extra': all_strings.right_extra,
                            'bearings': all_strings.right_bearings},
                    "battle":
                            {'current': False, 'solved': False,
                            'stone_here': True, 'talked': False,
                            'intro': all_strings.battlefield_intro,
                            'extra': all_strings.battlefield_extra_start,
                            'bearings': all_strings.battlefield_bearings1},
                    "dining":
                            {'current': False, 'solved': False,
                            'stone_here': True, 'read': False,
                            'intro': all_strings.dining_room_intro,
                            'extra': all_strings.dining_room_extra_start,
                            'bearings': all_strings.dining_room_bearings_start},
                    "butcher":
                            {'current': False, 'solved': False,
                            'stone here': True, 'touched meat': False,
                            'took pig': False, 'took meat': False,
                            'talked' False,
                            'intro': all_strings.butcher_intro,
                            'extra': all_strings.butcher_extra_start,
                            'bearings': all_strings.butcher_bearings_start},
                    "race":
                            {'current': False, 'solved': False,
                            'stone here':True, 'rock here': True,
                            'thrown': False,
                            'intro': all_strings.racetrack_intro,
                            'extra': all_strings.racetrack_extra_start,
                            'bearings': all_strings.racetrack_bearings_start},
                    "alone":
                            {'current': False, 'solved': False,
                            'stone here': True, 'final_response': False,
                            'good_text_up': False, 'sad_text_up': False,
                            'projector_power': False, "projector_on": False,
                            "projector_open": False, "not_chatted": True,
                            'stone_available': False,
                            'intro': all_strings.alone_intro,
                            'extra': all_strings.alone_extra_start,
                            'bearings': all_strings.alone_bearings_start},
                    "world":
                            {'current': False, 'solved': False,
                            'stone here': True, 'talked': False,
                            'intro': all_strings.world_intro_start,
                            'extra': all_strings.world_extra_start,
                            'bearings': all_strings.world_bearings_start}
                    }
