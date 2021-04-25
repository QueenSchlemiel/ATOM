#notes
# ctl + shft + b to run
# ctl + s to save

print("Hello World")

#string and if
string = "hello"
print(string)
if string == "hello":
    print("World")

#learnpython.org
#variables and types
print("\nVARIABLES AND TYPES")
myInt = 7
print(myInt)

myFloat = 7.0
print(myFloat)
myFloat = float(7)
print(myFloat)

#operators on strings and numbers
varOne = 1
varTwo = 2
varThree = varOne + varTwo
print(varThree)

string1 = "hello"
string2 = "world"
string3 = string1 + " " + string2
print(string3)

#Exercise
print("\nExercise")
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

#Lists
print("\nLISTS")
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist)
print(mylist[1]) #should print 2

#loop for list
for x in mylist:
    print(x)

#Exercise
print("\nExercise")
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

#Basic operators
#python does follow PEMDAS
print("\nBASIC OPERATORS")
number = 1 + 2 * 3 / 4.0
print(number)

#modulo
remainder = 11%3
print(remainder)

#power
squared = 7**2
cubed = 2**3
print(squared)
print(cubed)

#python also supports multiplying strings
lotsofhellos = "hello" * 10
print(lotsofhellos)

#operators with Lists
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

#Python also supports forming new lists with a repeating sequence using multiplication
print([1,2,3] * 3)

#Exercise
print("\nExercise")
x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

#String Formatting
print("\nSTRING FORMATTING")
name = "Laura"
print("Hello, %s!" % name)

age = 25
print("%s is %d years old." % (name, age))

#Basic String operations
astring = "Hello World!"
astring2 = 'Hello World!'

print("single quotes are ' '")
print(len(astring))

print(astring.index("o"))
print(astring.count("l"))

print(astring[3:7])
print(astring[3:7:2])

print(astring[::-1]) #reverses string
print(astring.upper())
print(astring.lower())

print(astring.startswith("Hello")) #determines if it starts with the param
print(astring.endswith("asdfasdfasdf")) #determines if ends with param

aFewWords = astring.split(" ") #splits on the space
print(aFewWords)

#Conditions
print()
print("CONDITIONS")
x = 2
print(x == 2) #determines if x is 2
print(x == 3) #determines if x is 3
print(x<3)

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

statement = False
statement2 = True
if statement is True:
    print("Statement is True")
elif statement2 is True:
    print("Statement2 is True")
else:
    print("Neither statement is true")

x = [1,2,3]
y = [4,5,6]
z = [1,2,3]
print()
print(x == y)
print(x == z)
print(x is y) #is matches the instances not the items in the variable
print(x is z)

print()
print(not False)
print((not False) == (False))

#Loops
print()
print("LOOPS")

primes = [2,3,5,7]
for prime in primes:
    print(prime)

print()
for x in range(5):
    print(x)
print()
for x in range(3,6):
    print(x)
print()
for x in range(3,8,2):
    print(x)

print()
count = 0
while count<5:
    print(count)
    count += 1

#break and continue statements
#break exits a loop
#continue skips block and starts loop again
print()
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

print()
for x in range(10):
    if x%2 == 0:
        continue
    print(x)

#can use else in loops
print()
count=0
while(count<5):
    print(count)
    count += 1
else:
    print("count value reached %d" %(count))

print()
for i in range(1,10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

#Exercise
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

print()
for i in numbers:
    if (i==237):
        break
    if (i%2==0):
        print(i)

#Functions
print()
print("FUNCTIONS")

def my_function():
    print("Hello from my function")

def my_args_func(user, greet):
    print("Hello, %s, from the function. I wish you %s" %(user,greet))

def sum(a,b):
    return a+b

my_function()
my_args_func("Laura", "a great day")
x = sum(1,2)
print(x)

#classes and objects
print("CLASSES AND OBJECTS")
