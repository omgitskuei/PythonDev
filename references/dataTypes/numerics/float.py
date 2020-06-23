# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x = 1.10
y = 1.0
z = -35.59

# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))


#You can use str.format() to specify decimal points.
a=2.1291
b="{0:0.2f}".format(a)
print(b) #Notice I asked it for 2 decimal points and it ROUNDED UP.
