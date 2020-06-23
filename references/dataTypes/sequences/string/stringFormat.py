

# In[1]: %-formatting
#The %s takes the next argument (in this case "name") and prints as string, %d takes next numeric and prints it
name = "John"
age = 26
nationality = 'Taiwan'
print("%s is %d years old from %s"%(name, age, nationality))


# In[2]: str.format()
# Syntax "{listIndex(es)}".format(list)
# str.format() is another option other than %-format for getting an output
a="hello"
print("{}".format(a))

# str.format() command can actually take many item (a,b,c,d,e) and combine them however you want as dictated in the {}s.
a, b, c, d, e="hello", "my", "name", "is", "Kuei"
print("{}".format(a, b, c, d, e))

# str.format() also comes with an index function; see below how I output (b) by calling the 2nd index (1) in {}.
# the default is {0}, and each bracket {} only calls out one variable (one of a, b, c, d, e)
print("{1}".format(a, b, c, d, e))				# prints 'my'

# I used the index feature of str.format() to rewrite the sentence.
print("{0}, {4} {3} {1} {2}".format(a, b, c, d, e))


# In[3]: Decimal control
# str.format() can specify how many decimal points;
# formula is {index:0.Xf}.format(value) where X is howManyDecimals, f for float
# eg. prints 5.00
print("{:0.2f}".format(5))
# eg. prints 5.0000
print("{:0.4f}".format(5))


# In[4]:
# A comparison of using str.format() and print(), and just using print().
hour="9am"
day=29
month=9
year=2019
print("My Python class began on {0}/{1}/{2}.".format(day, month, year, hour))
# See how print is comparitively messier, since it's picky about TYPE.
# You need the '+' sign to link strings together,'str' must be used to convert the numbers to stringsd, and you need to use "," comma's to link two variables together or numbers. Eg. print("total", totalNum)
day=29
month=9
year=2019
print("My Python class began on "+ str(day)+"/"+str(month)+"/"+str(year)+".")
#You could get away without writing the str() and +, and just use commas for everything but it will mess with formatting
print("My Python class began on",day,"/",month,"/",year,".  <-- unremovable spaces present w/o converting values to strings")
