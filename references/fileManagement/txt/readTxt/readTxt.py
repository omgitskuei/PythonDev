"""
Python Read Txt
omgitskuei
Aug 4th 2021
https://www.w3schools.com/python/python_file_handling.asp
https://www.kite.com/python/answers/how-to-read-a-text-file-into-a-list-in-python
"""

"""
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)

To open a file for reading it is enough to specify the name of the file:
f = open("demofile.txt") # same as ...
f = open("demofile.txt", "rt")
"""

# In[1]
"""
Read entire file, as one String
"""
# Call file.read() to return the entire content of file as a string.
file = open("testReadTxt.txt", "rt")
print(file.read())
# prints:
# OMG
# ONE
# TWO
# THREE
# butts as ass

file = open("testReadTxt.txt", "rt")
print(type(file.read()))
# <class 'str'>

file = open("testReadTxt.txt", "rt")
# Call str.split(sep) with this string as str to return
# a list of the values of the file split by sep.
list = file.read().split("\n")
print(list)
# ['OMG', 'ONE', 'TWO', 'THREE', 'butts as ass', '']


# In[2]
"""
Read entire file, line by line
"""
# Note: If the entire content of the file is all on one line,
# file.readlines() will return a list containing one item
# instead of a list of individual items.
file = open("testReadTxt.txt", "rt")
print(file.readlines())
# ['OMG\n', 'ONE\n', 'TWO\n', 'THREE\n', 'butts as ass\n']


# In[3]
"""
Read Only Parts of the File
"""
file = open("testReadTxt.txt", "rt")
print(file.read(5))
# prints:
# OMG
# O

file.close()
