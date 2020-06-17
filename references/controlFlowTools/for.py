# The for statement in Python differs from what you may be used to in C or Pascal.
# Rather than always iterating over an arithmetic progression of numbers,
# or giving let user define both the iteration step and halting condition (as C),
# NOTE: Python’s for statement iterates over items of ANY sequence
# (a list or a string), in the order that they appear in the sequence.

# Measure some strings (returning each of their lengths):
words = ['cat', 'door', 'screen']
for w in words:
	print(w, len(w), )



# Code that modifies a collection while iterating over that same collection can be tricky to get right. Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection:
# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
