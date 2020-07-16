aSet = set("apple", "tuna", "sandwich")
# aSet[0] = "berries" - would cause error
# print(aSet+aSet) set does not support + or * operants

# Removes the first one from set
# eg. removes 'apple' first, then 'tuna', lastly removes 'sandwich' )
aSet.pop()
# if you pop() an empty set, error KeyError: 'pop from an empty set'
