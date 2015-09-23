class MainMenu(object):

    options = {"New Game": pass, "Save Game": pass, "Load Game": pass}

    def run(self):
        pass

class SavedGame(object):

    items = []
    failed_puzzles = 0
    room_by_room = {"starting":
                            {'current': False, 'start': False, 'pen'"': False},
                    "middle":
                            {'current': False},
                    "door":
                            {'current': False, 'door open': False,
                            'attempted door': False,
                            'touched indentations': False
                            'bag': False,
                            'Stone of Peace': False, 'Stone of Silence': False,
                            'Stone of Respect': False,
                            'Stone of Practice': False,
                            'Stone of Friendship': False,
                            'Stone of Compassion': False},
                    "left":
                            {'current': False, 'racetrack open': False},
                    "right":
                            {'current': False, },
                    "battle":
                            {'current': False, 'solved': False,
                            'stone here': False,},
                    "dining":
                            {'current': False, 'solved': False,
                            'stone here': False,},
                    "butcher":
                            {'current': False, 'solved': False,
                            'stone here': False,},
                    "race":
                            {'current': False, 'solved': False,
                            'stone here': False,},
                    "alone":
                            {'current': False, 'solved': False,
                            'stone here': False,},
                    "world":
                            {'current': False, 'solved': False,
                            'stone here': False,}
                    }
