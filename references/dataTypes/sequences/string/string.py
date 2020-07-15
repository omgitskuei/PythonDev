# Strings count as sequence type because it can be indexed and sliced

""" Strings are immutable """
# NOTE: While they're sequences, Strings in Python are immutable/cannot be changed*
word = 'Python'
word[0] = 'J'		# executing this line will lead to TypeError;
# TypeError: 'str' object does not support item assignment

# *Immutable means the Type string (a and b) doesn't retain its ID (aka memory location) after it's given new values
a=1
print(id(a))
a=2						# what's happening here isn't changing a's value 1 to 2 ...
print(id(a))			# ... more like creating a new a with new value 2 that overrides the previous a

a=1						# NOTE: how the same 'number value' 1 has the same ID as
b=1						# each other regardless of variable names being different (a and b)
print(id(a))
print(id(b))
print(a is b)			# NOTE: the 'is' logic compares IDs

# if you need a new string, just make one
word = 'Python';
word = 'J' + word[1:];		# prints 'Jython', string word is overriden
print(word);

# String variables can be declared either by using single or double quotes:
x = "John"
# is the same as
x = 'John'

#  \ can be used to escape quotes:
# use \' to escape the single quote...
>>> 'doesn\'t'  			# prints "doesn't"
 # ...or use double quotes instead
>>> "doesn't" 				# prints "doesn't"
>>> '"Yes," they said.'		# prints '"Yes," they said.'
>>> "\"Yes,\" they said."	# prints '"Yes," they said.'
>>> '"Isn\'t," they said.'	# prints '"Isn\'t," they said.'


# NOTE: String literals can span multiple lines.
# One way is using triple-quotes: """...""" or '''...'''.
# End of lines are automatically included in the string, but it’s possible to
# prevent this by adding a \ at the end of the line.
# The following example:
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# produces the following output (note that the initial newline is not included):
# Usage: thingy [OPTIONS]\
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to

# this """\ ...some text""" is the same as;
print("\
Usage: thingy [OPTIONS]\
     -h                        Display this usage message\
     -H hostname               Hostname to connect to
")


# NOTE: Strings can be repeated with *
# eg. 3 times 'um', followed by 'ium'
>>> 3 * 'um ' + 'ium'	# answer = 'um um um ium'


# NOTE: 2 string literals will auto-concatenate
# string literals (i.e. the ones enclosed between quotes)
>>> 'Py' 'thon'
# 'Python'
# This feature is particularly useful when you want to break long strings:
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text	# answer = 'Put several strings within parentheses to have them joined together.'


# NOTE: This only works with literals (does not work with variables)
>>> prefix = 'Py'
>>> prefix 'thon'  # can't concatenate a variable and a string literal, leads to SyntaxError: invalid syntax

# The built-in function len() returns the length of a string:
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)		# prints 34

# Multiplying Strings
# what’s 10 multiplied by  a?
print(10 *  'a') 			# prints aaaaaaaaaa
# applications include standardized whitespace
spaces =  ' '  * 25
print('%s 12 Butts Wynd'  % spaces)		# looks like its right-aligning text
print('%s Twinklebottom Heath'  % spaces)
print('%s West Snoring'  % spaces)
print()
print('Dear Sir')
print()
print('I wish to report that tiles are missing from the')
print('outside toilet roof.')
print()
print('Regards')
print('Malcolm Dithering')

# Applications for .find(""); extracting substring
data="From:User Lee (user@company.com) Sat Jan 5 09:14:16 2016"
begIndex=data.find("(")
endIndex=data.find(")")
print(begIndex)
print(endIndex)
email=data[begIndex+1:endIndex]
print(email)
