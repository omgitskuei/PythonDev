
#Conditional statements
x=2
y=-3
for i in range(5):
    print("x", x, "y", y, "| i", i, "| x and y", bool(x and y), "| x or y", bool(x or y), "\n")
    i+=1
    x-=1
    y+=1
	#so, bool(x and y) is True so long as BOTH x and y are not 0's, bool(x or y) is True so long as AT LEAST one is not 0.

print(bool(0));
print(bool(1));
print(bool(3 and 2));
print(bool(1 or 0), bool(0 or 0));



# In[5]:


#if statements
#formula: if expression:
#             statements
#statements are run if the expression is TRUE
user="Kuei"
pwd="123"
if user=="Kuei" and pwd=="123":
    print("Welcome", user)

#if else
#formula: if expression:
#             statements
#         else:
#             statements
#only will run else statement if expression is FALSE, one of them will always run
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
#elif
#can add multple if's, ones after the first are elif not more if's


# In[10]:


#while loop
count=0
while count<9: #runs the print-count 9 times (SAME), since 9 is exclusive BUT it starts at 0
    print("count", count)
    count=count+1 #or count+=1
print("finished")


# In[27]:


#for loop
#can take string, tuple, list
#it operates expression for each item in sequence, and repeats going to the next item in sequence, UNTIL no item left
#Below are 3 ways of writing a for loop that repeats 3 times
for var in [1, 2, 3]:
    print(var)

for i in range(3):
    print(i)

list1=[1,2,3]
for i in range(len(list1)):
    print(i)


# In[16]:


#nested loops
#nested while:

#nested for:
for i in range(1, 5):         #range(1,5) means 1, 2, 3, 4
    for j in range(1, 5):     #... NO 5!!!!!!!!!!!!, still exclusive and still defaults to 0
        x=i*j
        print(i, j, x)
    print()                    #total number times ran is 4*4





#break
#say the break was inside the loop condition, so true, would kick program out of loop, as if the loop condition was false
for num in [31, 23, 12, 21]:
    if num%2==0:
        print("Data contains even")
        break
    else:
        print("num=", num)
#continue
#continue, if yes, sends program back to loop condition, skipping whatever was supposed to come next


# In[13]:


#+, *, [index], slice [beginning:end], in, not in, r/R, len(),
a="Hello"
b="Python"
c="Hello \n World"
print("+ "+a+b)
print("* "+a*2)
print("\n "+c)
print("1 index "+a[1])
print("0 to 4 index "+ a[0:4])


# In[140]:


#Immutable means the Type (a and b) doesn't retain its ID (aka memory location) when you make changes to its values
a=1
a=2
print(id(a))
print(id(a))
print()
#Note how the same 'number value' 1 has the same ID as each other
a=1
b=1
print(id(a))
print(id(b))
#Note how the logic compares ID's
print(a is b)


#
data="From:User Lee (user@company.com) Sat Jan 5 09:14:16 2016"
begIndex=data.find("(")
endIndex=data.find(")")
print(begIndex)
print(endIndex)
email=data[begIndex+1:endIndex]
print(email)


# In[59]:


#List is a sequence of mutable (retains ID) objects and uses [] square brackets, separated values via comma
CurrentPlayers = ["Bob", "Dylan"]
print(CurrentPlayers)

#Lists can contain int, float, string, etc. Lists can also contain other lists - more on that below.
Ingredients = [1, "potato", 3, "eggs", 2, "chicken breasts", 20.50, "grams of salt"];
print("Ingredients", Ingredients)

#Lists can also be created empty
NewPlayers = [];
print("empty New", NewPlayers)

#Here we add list NewPlayers to the end of list CurrentPlayers with list1.extend(obj)
#There's also list1.append(obj) as well
NewPlayers = ["Ashley"]
CurrentPlayers.extend(NewPlayers) #Note, can use same line if separated with a semi-colon ;.
print("Current", CurrentPlayers)
CurrentPlayers.append(NewPlayers) #will also work
print("Current", CurrentPlayers)  #note extend and append are similar, different

#Lists have index features - remember, index starts at 0, and (X:Y) Y is EXCLUSIVE - this is why only "Dylan" is printed
print(CurrentPlayers[1:2])
#Remember that not specifying (X:Y) Y means it'll carry on til the end.
print(CurrentPlayers[1:])
#Also, (X:Y:Z) Z is used if you want to periodically skip indexes
print("Ingredients w/o Numbers", Ingredients[1::2]) #Starts on the 2nd value and skips every other value (removes nums)

#You can change a slice of a list
CurrentPlayers[0]="Bobby" #In the example, I'm over-riding Bobby over Bob, see how the changes 'stick'.
print("Updated Current", CurrentPlayers)
#Lists can contain other lists (on top of int, float, strings)
AllPlayers = [NewPlayers, 1201, CurrentPlayers, 250.0, "Guest"]
print("All", AllPlayers)
#The lists contained can be called in entirity or sliced
print("Just Current from All", AllPlayers[2])
print("Just 1st of Current from All", AllPlayers[2][0]) #Note AllPlayers[index for AllPlayers][index for CurrentPlayers]
#Can use negative indexes to count down from the end
print("2nd to last of Current", CurrentPlayers[-2])
print("Last of Current", CurrentPlayers[-1])
#len() is a function that counts how many variables there are in the (whatever you passed into the brackets)
print(len(CurrentPlayers)) #should give you 3; Bobby, Dylan, Ashley.
#You can 'add' lists to combine them into a single list - note that values are NOT sorted
print([1, 2, 3] + [2, 3, 4])
#You can 'multiply' lists to repeat the same values - note you cant 'divide' the list, that just gives an error
print("3* Current", CurrentPlayers * 2)

#Remember Membership Operators; tests if value is in data sequence, True or False
print(2 in [1, 2, 3, 4])  #True
#

#List comprehension - you can use mathematical equation for writing a list
#Below is an example a list of values where each index is squared, and the list has goes from 0*0, 1*1, etc, up to 9*9
S = [x**2 for x in range(10)]
print(S)


# In[96]:


tuple_year=0
for i in range(2020):
    j=i+1
    if((not j%100)) and j%4
t = {x^2 : x in }


# In[ ]:


#Like lists, tuples can hold values of different types
tup1=("Python", 131, 3456.23, "beep")
#Similarly, tuples can also be empty
tup2=()
#But if there's ONLY ONE value, a comma MUST follow
tupOnly1=("Wow",)
#Calling a value from a tuple using index MUST USE [], same as list, NOT ().
#tuple1(2) would be an error.
print(tup1[2])
#A tuple is a sequence of immutable objects
#Unlike list, you can't make direct edits to values inside the tuple.
#tuple1[2]=23.3456 would be an error.
#We can add to a tuple using +, but its ID will be different, hence Immutable
print(tup1)
print("old tuple1 ID", id(tup1))
tup1 = tup1 + ("AI", "exp")
print(tup1)
print("new tuple1 ID", id(tup1))
#You can actually hold a list as one of the values of a Tuple
tup3 = ("Python", [22, 1, 2], 77)
#And you can also call a value from the list inside the tuple
print(tup3[1][2])
#Why do you want to use Tuple over List? Tuple doesnt let people make changes as easily. Useful for exams.

#

#


# In[ ]:


#Dict is mutable (like Lists), non sequence, and Key (aka variable name) and its values are separated by : colon not = sign
dict1 = {"Name":"III", "Year":1979, "Class":"A"}
print(dict1["Name"])

dict2=dict(one=1, two=2, three=3)
print(dict2["two"])
#outputs 2



#sorted

#dict(mapping|iterable|**kwarg)


# In[ ]:


dict2.get("one", 0)

#defaults returns 0 if theres no "thing " in the dict, say "ONE111" wouldnt be in the dict, id receive a 0


# In[ ]:


dict2.popitem()


# In[ ]:


#library named thesaurus will return a value when given a key
#Eg. I give thesaurus "sword", it looks it up and returns the value "blade"
#remember that the KEY MUST BE UNIQUE
thesaurus={"mean":"unkind", "welcoming":"likable", "sword":"blade"}
print(thesaurus["mean"])
#remember that the format of libraries is always KEY:VALUE
#because format is always KEY:VALUE, giving the thesaurus "unkind" WILL NOT return "mean", because "unkind" is not a key
#print(thesaurus["unkind"])
print(thesaurus["welcoming"])
#print(thesaurus["blade"])
print(thesaurus["sword"])


# In[ ]:


#defined a function called p that takes a string and prints it out.
def p(pstr):
    print(pstr)
p("Hi")


# In[ ]:


def sum_nums(n1, n2):
    print(n1)
    print(n2)
    return n1+n2

sum_nums(5,8)


# In[ ]:


a=sum_nums(3, 2)
p(a)


# In[ ]:


def bmi(kg, m):
    return "{0:0.2f}".format(kg/(m**2))
p(bmi(68, 1.7))

#you COULD just return the numbers without formatting them but that's not ideal.
def bm3(kg, m):
    return kg/(m**2)
p(bm3(68, 1.7))

#notice how you need the return, otherwise calling it with variables and printing gives you nothing
def bm3(kg, m):
    kg/(m**2)
p(bm3(68, 1.7))


# In[ ]:


#i = 0, 1, 2, runs 3 times total, 3 is exclusive
for i in range(3):
    p("a")


# In[ ]:


#function definition
def changeme(myvar):
    print("in function, before changes:", myvar)
    myvar=50
    print(id(myvar))
    print("in function, after changes:", myvar)
    return myvar
#this myvar (20) is immutable and is a global variable, is a separate var from the myvar in the "def changeme(myvar)" line
myvar=20
print(id(myvar))
#see how the ID for myvar outside the changeme function is different from the ID inside the function

changeme(myvar)
print("outside function:", myvar, "\n")

#you'd have to do myvar=changeme(myvar) to make sure the value over-rides the original global variable, if thats what you want.
#I'll make another global variable to 'receive' the returned results
myvar2=changeme(myvar)
print("outside function2:", myvar2)


# In[ ]:


#list, set, dict are mutable, same ID so changes to it via functions WILL STICK, unlike above
def changeme(myvar):
    print("in function, before changes:", myvar)
    myvar[2]=50
    print("in function, after changes:", myvar)
    return myvar
#this myvar is immutable, and is a separate variable from the myvar in the "def changeme(myvar)" line
myvar=[10, 20, 30, 60]
changeme(myvar)
#at this point, myvar has been changed by changeme, and this sticks even outside the function
print("outside function:", myvar, "\n")
myvar2=changeme(myvar)
print("outside function2:", myvar2)


# In[ ]:


{'foo'}


# In[ ]:


set('foo')


# In[ ]:


set('foo')


# In[ ]:


x = set(['foo', 'bar', 'baz', 'foo', 'qux'])
x


# In[ ]:


s = 'quux'

list(s)
['q', 'u', 'u', 'x']
set(s)
{'x', 'u', 'q'}


# In[ ]:


#Alternately, a set can be defined with curly braces ({}):

x = {<obj>, <obj>, ..., <obj>}


# In[ ]:


#Observe the difference between these two set definitions:
{'foo'}
{'foo'}

set('foo')
{'o', 'f'}

#A set can be empty. However, recall that Python,
#... interprets empty curly braces ({}) as an empty dictionary,
#... so the only way to define an empty set is with the set() function:
x = set()
type(x)
<class 'set'>
x
set()

x = {}
type(x)
<class 'dict'>

An empty set is falsy in Boolean context:
x = set()
bool(x)
False


# In[ ]:


#Exceptions
#There's two kinds of errors;
#1) syntax (parsing errors)
#2) exceptions (run time errors)
#Python already comes with premade exceptions, which I can read about at docs.python.org/3/library/exceptions.html
#SyntaxError, ZeroDivisionError, etc

#try:
#   stmt
#except Exception1:
#   if there's Exception1, then execute this block
#except Exception2:
#   if exp2, execute block
#

#else

#finally


# In[45]:


#Read/Writing files
#Open/Create new file
fo = open('myfile.txt', "w")
print('File Name:', fo.name)
#Open file, similar to w, but x will make error message if no file found, will not create new)
#fo = open('myfile.txt', "x")

#Write file
fo.write('Python is a great language')

#Read file
fo = open("myfile.txt", "r")
str = fo.read(10)
print("read string:", str)

#Close file
fo.close


# In[43]:


fo = open('myfile.txt', "r+")
while True:
    line=fo.readline() #reads one line at a time
    if not line:
        break
    print(line, end='')  #there's an automatic enter at the end of print. end='' removes the auto-enter
fo.close


# In[46]:


fo = open('myfile.txt', "r+")
while True:
    line=fo.readlines() #reads multiple lines at once
    if not line:
        break
    print(line, end='')  #there's an automatic enter at the end of print. end='' removes the auto-enter
fo.close


# In[47]:


fo = open('myfile.txt', "r+")
line=fo.readlines() #reads multiple lines at once
print(line, end='')  #there's an automatic enter at the end of print. end='' removes the auto-enter
fo.close


# In[49]:


fo = open('myfile.txt', "r+")
line=fo.readlines() #reads multiple lines at once
print(line, end='')  #there's an automatic enter at the end of print. end='' removes the auto-enter
fo.close


# In[50]:


fo = open('myfile.txt', "r+")
line=fo.readline() #reads one line at once
print(line, end='')  #there's an automatic enter at the end of print. end='' removes the auto-enter
fo.close


# In[51]:


try:
    fp = open('myfile.txt', 'r')
    data = fp.read()
    print('Content:')
    print(data)
except:
    print('Error:File IO error')
finally:
    fp.close


# In[54]:


with open("myfile.txt", "r") as fp:
    data=fp.read()
    print('Content:')
    print(data)
fp.close()


# In[58]:


import urllib.request
x = urllib.request.urlopen('https://kai.one/colab_quiz_18.txt');
print(x.read().decode('utf-8'));


# In[ ]:
