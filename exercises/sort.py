def sort(listInt, orderKeyword):
	"""Sorts the passed list in ascending/descending order"""
	try:
		listSize = int(len(listInt))
		# declaring new lists (alternatively, listName = [])
		incrOrderKeys = list(("asc","a","ascending","increasing","incr","i"))
		decrOrderKeys = list(("desc","d","descending","decreasing","decr","d"))
		print("Passed params: listInt =",listInt,"( listSize =",listSize,") orderKeyword =", orderKeyword,"\n")

		for incrIndex in range(0, listSize-1, 1):

			swapped = bool(False)

			for swapIndex in range(incrIndex+1, listSize, 1):
				print(">> listInt[", incrIndex,"] =",listInt[incrIndex],", listInt[", swapIndex,"] =",listInt[swapIndex])

				# keyword 'in' to match list elements
				if orderKeyword in incrOrderKeys and listInt[incrIndex] > listInt[swapIndex]:
					print('>>> Swapping', listInt[incrIndex], "and", listInt[swapIndex])
					listInt[incrIndex], listInt[swapIndex] = listInt[swapIndex], listInt[incrIndex]
					swapped == True
				elif orderKeyword in decrOrderKeys and listInt[incrIndex] < listInt[swapIndex]:
					print('>>> Swapping', listInt[incrIndex], "and", listInt[swapIndex])
					listInt[incrIndex], listInt[swapIndex] = listInt[swapIndex], listInt[incrIndex]
					swapped == True

			if swapped == True:
				print(">>>> Current listInt =", listInt,"\n")
			else:
				print(">>>> No Swaps occured,", "Current listInt =", listInt,"\n")

		print("Result =", listInt)
	except Exception:
		pass

	return listInt

# Driver
order = 'asc'
listInt = [10,6,5,4]
sort(listInt, order)
