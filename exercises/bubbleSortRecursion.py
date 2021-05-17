# In[1]: Python program for implementation of Bubble Sort

# NOTE: bubble_sort uses recursion to repeat through each element

def bubble_sort(listt, order):
	for i, num in enumerate(listt):
		try:
			if order == 1:
				if listt[i+1] < num:
					listt[i] = listt[i+1]
					listt[i+1] = num
					bubble_sort(listt, 1)
			else:
				if listt[i+1] > num:
					listt[i] = listt[i+1]
					listt[i+1] = num
					bubble_sort(listt, 0)
		except IndexError:
			pass
	return listt

listt = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(listt, 1)

print("Sorted array:");
for i in range(0, len(listt)):
	print(listt[i], end=' ')
