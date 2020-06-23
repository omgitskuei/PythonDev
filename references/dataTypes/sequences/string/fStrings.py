#f-strings
#formula f'[{expression}]'
a="eggs"; b="toast"
print(f'{a} and {b} are amazing.')

#f-strings are capable of calculating inside brackets
print(f'[{1+3}] is 1+3 is 4.')

#f-strings lets me call the comedian dictionary and fill in data
comedian = {"name": "Eric Idle", "age": 74}
f"The comedian is {comedian['name']}, aged {comedian['age']}."
#note that the comedian['name'] part can't use "" because "" are already in use by the f-string.
