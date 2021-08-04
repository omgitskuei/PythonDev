"""
Python Write Txt
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
Write (overwrite contents w new ones)
"""
file = open("testWriteTxt.txt", "wt", newline='?')
print(type(file))
# <class '_io.TextIOWrapper'>

file.write("omg")
file.write("omg2")
# omgomg2


# In[2]
"""
Write (append new lines)
"""
file = open("testAppendTxt.txt", "a")
file.write("omg?")
file.write("omg??")


file.close()
