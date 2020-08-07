'''
Given a list:
ingredients = ['snails', 'leeches', 'gorilla belly-button lint', 'caterpillar eyebrows', 'centipede toes'];

Create a loop that prints out the list (including the numbers):
1 snails2 leeches3 gorilla belly-button lint4 caterpillar eyebrows5 centipede toes
'''

ingredients = ['snails', 'leeches', 'gorilla belly-button lint', 'caterpillar eyebrows', 'centipede toes'];
stringBuilder = "";
count = 0;
for eachElement in ingredients:
    count = count+1;
    stringBuilder = stringBuilder + (str)(count) + " " + eachElement;
print(stringBuilder);
