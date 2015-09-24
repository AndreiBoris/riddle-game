class Tester(object):

    def __init__(self, name, number):
        self.name = name
        self.number = number

hat = Tester('hat', 1)
brick = Tester('brick', 2)
bob = Tester('bob', 3)
madrid = Tester('madrid', 4)
lo = Tester('lo', 5)
jeez = Tester('jeez', 6)

for room, key in [(hat, 1), (brick, 2),
            (bob, 3), (madrid, 4),
            (lo, 5), (jeez, 6)]:
    print key, room.name
