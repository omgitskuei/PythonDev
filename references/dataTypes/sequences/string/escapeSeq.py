# In[1]: Escape sequences/characters, Syntax

# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.

# NOTE: The escape character can be written into a word
a="Yes \naps No";
print(a)					# prints Yes [Enter] aps No


# In[2]: Escape sequences, Reminder

# WITHOUT print(), special characters like \n for [newline] are IGNORED.

s = 'First line.\nSecond line.'  # \n means newline
s  						# prints 'First line.\nSecond line.'
print(s)  				# prints 'First line.
								# Second line.'


# In[3]: Ignoring escapes

# NOTE: Using 'raw String' to ignore special characters
# If you don’t want characters prefaced by \ to be interpreted as special
# characters, you can use raw strings by adding an r before the first quote:
>>> print('C:\some\name')  # here \n means newline!
# prints
# C:\some
# ame
>>> print(r'C:\some\name')  # note the r before the quote
# prints
# C:\some\name


# In[3]: Escape sequences, Dictionary

#\n - newline / Enter / Carriage return
a="Yes \n and No";
print(a)

# \\ - prints (\)
string2 = 'http:\\\\www.buycarrots.com\\cart';
print(string2);					# prints http:\\\www.buycarrots.com\cart

# \' - prints  single quotes(')
string2 = 'Those are some \'phat\' dogs!';
print(string2);

# \" -
single_quote_str =  'He said, "Aren\'t can\'t shouldn\'t wouldn\'t."';
double_quote_str =  "He said, \"Aren't can't shouldn't wouldn't.\"";
print(single_quote_str);		# prints He said, "Aren't can't shouldn't wouldn't."
print(double_quote_str);		# prints He said, "Aren't can't shouldn't wouldn't."

# \a - bulletpoint
string = 'What if I \a threw a ball at your face, \a slap your face with my ball, and \a screamed at your face>?';
print(string);
string2 = 'Groceries List: \n\a Carrot \n\a Broccoli \n\a Spinach';
print(string2);

# \f - form feed
# Form feed is a page-breaking ASCII control character.
# It forces the printer to eject the current page and to continue printing at the top of another.
string2 = '... end of page 1.\fBeginning of page 2 ... end of page 2.\fBeginning of page 3';
print(string2,end='');
# The end='' is used to prevent Python from printing an additional new line after the form feed character.
print('\f',end='')

# \r - Carriage Return

# \t - Tab
string = 'This is a tab\t with some more words afterwards.';
print(string);

# \000 - space
string = 'How does the cat me\000ow? Like this?';
print(string);

# \b - backspace (???)
string2 = '----\bCarrot----\bSpinach';
print(string2);

# \v - the male gender symbol?
string = 'How does t\vhe cat meow? Like this?';
print(string);
