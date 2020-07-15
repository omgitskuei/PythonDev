# NOTE: if bool(x) is given a number, 0 means FALSE and ANYTHING ELSE means TRUE
print(bool(-1));		# true
print(bool(0));			# false
print(bool(1));			# true
print(bool(1.5));		# true

print(bool(0 and 0));	# false
print(bool(0 and 1));	# false
print(bool(2 and 3));	# true

print(bool(0 or 0));	# false
print(bool(0 or 1));	# true
print(bool(2 or 3));	# true
print(bool(1 or 0), bool(0 or 0));		# true false

# When you use  bool  for other values, like strings, it returns  False if there’s no value for the string (in other words, the keyword  None or an empty string). Otherwise, it will return  True, as shown here:
print(bool(None)) 		# False
print(bool('a'))		# True
print(bool(' ')) 		# True
