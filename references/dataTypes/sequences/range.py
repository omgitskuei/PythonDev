The  range  function doesn’t actually create a list of numbers; it returns an  iterator, which is a type of Python object specially designed to work with loops. However, if we combine  range  with list, we get a list of numbers. >>>  print(list(range(10, 20, 2))) [10, 12, 14, 16, 18]

You don’t need to stick to using the  range  and  list  functions when  making  for  loops. You could also use a list you’ve already created, such as the shopping list from Chapter 3, as follows:
>>>  wizard_list = ['spider legs',  'toe of frog',  'snail tongue', 'bat wing',  'slug butter',  'bear burp']
>>>  for  i  in  wizard_list:
print(i)
spider legs toe of frog snail tongue bat wing slug butter bear burp

hugehairypants = ['huge',  'hairy',  'pants']
for  i  in  hugehairypants:
    print(i)                  #
    for  j  in  hugehairypants:    # These lines are the FIRST block.
        print(j)              #


>>> x = 45v
>>> y = 80w
while x < 50 and y < 100:
        x = x + 1
        y = y + 1
        print(x, y)

while  True:
    ‘’’some code’’’
    if  some_value ==  True:
        break
