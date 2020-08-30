"""
Using the Pickle module.

It's used to read/write Python objects from/to file.

Created on Sun Aug 30 11:01:06 2020.

@author: omgitskuei
"""

# -*- coding: utf-8 -*-

import pickle

"""
[pickle.dump()] can SAVE this map [game_data] to an opened file.

pickled Python objects are stored as binary files, which aren't always
readable for humans.
"""
game_data = {
    'player-position':  'N23 E45',
    'pockets': ['keys',  'pocket knife',  'polished stone'],
    'backpack': ['rope',  'hammer',  'apple'],
    'money': 158.50
    }

save_file = open('save.dat', 'wb')
# we open the file save.dat, the wb param means "write the file in binary mode"
pickle.dump(game_data, save_file)
# we use pickle.dump(dataToWrite, targetFile) to pass in the map and the file.
save_file.close()

"""
[pickle.load(openedFile)] function takes information written to file and
convert it to values Python can use.
"""
load_file = open('save.dat',  'rb')
loaded_game_data = pickle.load(load_file)
load_file.close()
print(loaded_game_data)
# {
# 'money': 158.5,
# 'backpack': ['rope', 'hammer', 'apple'],
# 'player-position': 'N23 E45',
# 'pockets': ['keys', 'pocket knife', 'polished stone']
# }
