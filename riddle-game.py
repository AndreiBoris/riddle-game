class Engine(object):

    def __init__(self, a_map):
        self.map = a_map

class Inventory(object):

    keys = ["key to sorrow", "key to gratitude"]

    def show(self):
        print "Your inventory:"
        for key in self.keys:
            print key
        if not self.keys:
            print "Nothing!"

    def add(self, new_key):
        self.keys.append(new_key)

    def clear(self):
        del self.keys[:]

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
inv = Inventory()
