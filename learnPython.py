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

#try again...
