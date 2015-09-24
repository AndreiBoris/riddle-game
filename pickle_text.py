import pickle

with open('saved.py', 'rb') as save_doc:
    saved_file = pickle.load(save_doc)
    print saved_file.rooms['start']['pen']
