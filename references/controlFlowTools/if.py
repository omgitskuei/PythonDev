# NOTE: An if … elif … elif … sequence is a substitute for
# the switch or case statements found in other languages.

# if-statements SYNTAX;
# if expression:		# if the expression is TRUE, statements are run
#     statements
user="kuei"
pwd="123"
if user=="Kuei" and pwd=="123":
    print("Welcome", user)
else:
    print("Go away.")


num=int(input("give num thnx"))
if num%2==0:
    if num%3==0:
        print("num divisible by 2 and 3")
    else:
        print("num divisible by 2, but not 3")
else:
    if num%3==0:
        print("num not divisible by 2, but is divisible by 3")
    else:
        print("num not divisible by 2, nor divisible by 3")


# NOTE: Short-hand if statement for single statements:
a = 3
b = 2
if a > b:
	print(a > b)	# prints True

# Example:
x = int(input("Please enter an integer: "))
if x < 0:
	x = 0
	print('Negative changed to zero')
elif x == 0:
	print('Zero')
elif x == 1:
	print('Single')
else:
	print('More')

"""Best practice; leave most broad condition last"""
# NOTE: Order of if statements matter!
	x=9
	if x < 50:
		print("<50")
	elif x < 30:
		print("<30")
	elif x < 10:
		print("<10")			# prints <50, which is wrong

	x=9
	if x < 10:
		print("<10")
	elif x < 30:
		print("<30")
	elif x < 50:
		print("<50")			# prints <10, which is correct
