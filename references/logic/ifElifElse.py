
number = 0
index = 0
while index < 6:
	if number < 3:
		print(number)
		print("number<3")
	elif number == 3:
		print(number)
		print("number=3")
	else:
		print(number)
		print("number>3")
	number = number + 1
	index = index + 1

# Short-hand if statement for single statements:
a = 3
b = 2
if a > b: print(a > b)	# prints True
