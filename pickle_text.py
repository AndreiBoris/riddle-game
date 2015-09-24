import pickle

with open('saved.py', 'rb') as save_doc:
    saved_file = pickle.load(save_doc)

print "Inventory: ", saved_file.items
print "Attempted World: ", saved_file.rooms['world']['attempted']
print "Attempted Battle: ", saved_file.rooms['battlefield']['attempted']
print "Attempted Race: ", saved_file.rooms['racetrack']['attempted']
print "Attempted Butcher: ", saved_file.rooms['butcher']['attempted']
print "Attempted Alone: ", saved_file.rooms['alone']['attempted']
print "Attempted Dining: ", saved_file.rooms['dining room']['attempted']
