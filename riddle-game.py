class Engine(object):

    def __init__(self, a_map):
        self.map = a_map

class Inventory(object):

    keys = []

    def show(self):
        # show which keys are currently posssesed
        pass

    def add(self):
        # add a key to the inventory
        pass

class Room(object):

    def inventory(self):
        # somehow access inventory
        pass

    def move(self):
        # move in various directions using Map
        pass

class Map(object):
    pass

the_map = Map()
game = Engine(the_map)
