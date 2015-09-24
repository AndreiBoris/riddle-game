import pickle

with open('saved.py', 'rb') as save_doc:
    retrieved = pickle.load(save_doc)

print retrieved.rooms['middle']['visited']
