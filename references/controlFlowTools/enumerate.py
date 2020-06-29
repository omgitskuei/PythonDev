for rating in PlayListRatings:
    if rating < 6:
        break
    print(rating)
	
In general for loops will be more appropriate when iterating over a list. If you need the index position as well you can use enumerate(). For example:

for i, rating in enumerate(PlayListRatings):
    if rating < 6:
        break
    print(f"Rating {str(i+1)}: {rating}")
