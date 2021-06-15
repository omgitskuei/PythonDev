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

# In[4]: A notable use for f-strings is they can short-hand print out
# variables for debugging.
aVar = "someText"
anotherVar = 1      # note: works with type other than String
lastVar = 41.44
# prints aVariable='someText'
print(f'{aVar=}',
      f'{anotherVar=}',
      f'{lastVar=}')