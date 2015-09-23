class MainMenu(object):

    options = {"New Game": pass, "Save Game": pass, "Load Game": pass}

    def run(self):
        pass

class SavedGame(object):

    items = []
    failed_puzzles = 0
    room_by_room = {"starting":
                            {'current': False, 'start': False, 'pen': False,
                            'intro': None, 'extra': None, 'bearings': None},
                    "middle":
                            {'current': False, 'intro': None, 'extra': None,
                            'bearings': None},
                    "door":
                            {'current': False, 'door open': False,
                            'attempted door': False,
                            'touched indentations': False, 'bag': False,
                            'intro': None, 'extra': None, 'bearings': None,
                            'Stone of Peace': False, 'Stone of Silence': False,
                            'Stone of Respect': False,
                            'Stone of Practice': False,
                            'Stone of Friendship': False,
                            'Stone of Compassion': False},
                    "left":
                            {'current': False, 'intro': None, 'extra': None,
                            'bearings': None},
                    "right":
                            {'current': False, 'racetrack open': False,
                            'intro': None, 'extra': None, 'bearings': None},
                    "battle":
                            {'current': False, 'solved': False,
                            'stone here': False, 'talked': False,
                            'intro': None, 'extra': None, 'bearings': None},
                    "dining":
                            {'current': False, 'solved': False,
                            'stone here': False, 'read': False,
                            'intro': None, 'extra': None, 'bearings': None},
                    "butcher":
                            {'current': False, 'solved': False,
                            'stone here': False, 'touched meat': False,
                            'took pig': False, 'took meat': False,
                            'talked' False, 'intro': None, 'extra': None,
                            'bearings': None},
                    "race":
                            {'current': False, 'solved': False,
                            'stone here': False, 'rock here': False,
                            'thrown': False, 'intro': None, 'extra': None,
                            'bearings': None},
                    "alone":
                            {'current': False, 'solved': False,
                            'stone here': False, 'final_response': False,
                            'good_text_up': False, 'sad_text_up': False,
                            'projector_power': False, "projector_on": False,
                            "projector_open": False, "not_chatted": True,
                            'stone_available': False, 'intro': None, 'extra':
                            None, 'bearings': None},
                    "world":
                            {'current': False, 'solved': False,
                            'stone here': False, 'talked': False,
                            'intro': None, 'extra': None, 'bearings': None}
                    }
