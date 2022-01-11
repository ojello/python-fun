# # Variable Practice
# from math import *
# age = "35"
# numbers = 23.432
# name = "Adi"
# is_male = True
# print("There was a man named " + name)
# print("And he was about " + age + " years old")

# # Creating a new line
# print("Giraffe\nAcademy")

# print("Giraffe\"Academy")

# # Concatenation
# phrase = "Halo"
# print(phrase + " is cool")

# # converts to lowercase
# print(phrase.lower())

# # converts to uppercase
# print(phrase.upper())

# # check if uppercase
# print(phrase.isupper())

# # check if lowercase
# print(phrase.islower())


# # figure out the length of the string
# print(len(phrase))

# # to get individual characters in a string
# print(phrase[0], phrase[1], phrase[2], phrase[3])  # H A L O

# # Index function - tells us where a specific character/string is located in a string.

# phrase = "Halo"
# print(phrase.index("a"))  # index place 1
# print(phrase.index("alo"))  # index place 1
# # print(phrase.index("x"))  # throws an error
# print(phrase.replace("Hal", "Elephant"))  # replaces Hal with Elephant.

# # Working with Numbers
# print(2)
# print(-2.123)
# print(3 + 4.5)

# print(3 * 4 + 5)
# print(3 * (4 + 5))
# print(10 % 3)  # remainder of 1

# my_num = 5
# print(my_num)
# my_num = -5
# # type coercion
# print(str(my_num) + " my favorite number")
# print(abs(my_num))

# # taking number to specific power
# print(pow(3, 2))

# # takes the highest number
# print(max(4, 6))

# # take the lowest number
# print(min(4, 6))

# # return the sqrt of a number
# print(sqrt(36))

# Getting input from the user
# age = str(input("Enter your age!: "))
# print("You are " + age)

# float allows decimal numbers
# int allows only whole numbers

## num1 = float(input("Enter a number: "))
# num2 = float(input("Enter a 2nd number: "))
# result = num1 + num2
# print(result)

# # Mad libs
# num_bal = str(input("Enter number of balloons you want: "))
# color = input("Enter a color: ")
# shape_bal = str(input("Enter the shape of the balloons you like! :"))


# print("I like " + color + shape_bal + "-shaped balloons")
# print("I would like to have " + num_bal + " balloons")

# Lists
from math import *
friends = ["Andrew", "Katy", "Amber", "Alice", "Ali", "Ali"]

# how can we access individual elements in a list
print(friends)

# print a specific element in a list
print(friends[1])

print(friends[1:])  # takes all the elements after index 1 + index 1

# will grab Katy and Amber but not the third element - Alice
print(friends[1:3])

# modifies the index 1 and change Mike
friends[1] = "Mike"

# List Functions
lucky_numbers = [4, 8, 15, 16, 23, 42]
print(lucky_numbers)
dogs = ["Ivy", "Graham", "Ashton"]
# extend function - allows you to take another list and append a list to it.
# friends.extend(lucky_numbers)

# Add another element to the end of the list
print(dogs.append("Anna"))

# insert function - takes the index, and the element you want to add.
friends.insert(1, "Kelly")
print(friends)

# remove function - remove()
friends.remove("Mike")
print(friends)

# clear function - clears the whole list
# friends.clear()

# pop function - gets rid of the last element
friends.pop()

# index function - check if an element is in the list
# print(friends.index("Gavin"))

# count function - shows how many times an element shows up in a list
print(friends.count("Ali"))

# sort function - sort the list in alphabetical order
friends.sort()
dogs.sort()


# reverse function - reverses the list
lucky_numbers.reverse()

# copies the list
friends2 = friends.copy()


# Tuples
# tuple is immutable - can't be changed/modified

coordinates = (4, 5)

# you can access the elements in a tuple
print(coordinates[1])

# Functions


def say_hi(name, age):
    print("Hello " + name + " you are " + str(age))


say_hi("bob", "90")


# Return Statements
def cube(num):
    return num*num*num


result = cube(4)
print(result)

# If statements
# If I leave my house if it's cloudy, I bring an
# umbrella otherwise I bring sunglasses


def weather(cloudy):
    if(cloudy == True):
        print("need umbrella")
    else:
        print("bring glasses")


weather(True)


is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a tall guy")
elif is_male and not is_tall:
    print("you are a short guy")
elif not is_male and is_tall:
    print("you are a tall woman")
else:
    print("you are a short woman")


def max_num(num1, num2, num3):
    if num1 > num2:
        print(num1 + " is the larger number")
        if num2 > num3:
            print(num2 + "is the largest number")
        else:
            print(num3 + " is the largest number")
    if num1 > num3:
        print(num1 + " is the largest number")


max_num(2, 4, 1)


# creating a dictionary
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
print(monthConversions["Nov"])
print(monthConversions.get("Luv", "Not a valid Key"))

# While Loop
i = 1
while i <= 10:
    print(i)
    i += 1
print("Done with loop!")

# Building a basic guessing game:
secret_word = "octopus"
guess = ""
# set a limit of how many times a user can use a word.
i = 1
if i < 3:
    while guess != secret_word:
        guess = input("Please keep trying :): ")
        i += 1
print("You win!")


pets = [("Ivy", 12), ("Graham", 1), ("Ming", 3), ("Oli", 3),
        ("Odette", 4), ("Lily", 5), ("Lady", 2)]

petsage = [name for (name, age) in pets if age <= 12]
print(petsage)


# Lists

primes = [2, 3, 5, 7, 11, 13]
primes.append(17)
primes.append(19)

# slicing lists
# slicing includes the value of slicing indexes but doesn't include the stopping index.

primes[2:5]  # 5,7,11
primes[0:6]  # 2, 3, 6, 11, 13 - will not include the final number

# combining lists - called Concatenation
numbers = [1, 2, 3, 4, 5]
letters = ["a", "b", "c", "d"]
lol = letters + numbers
# order matters in lists
# reversed version
funny = numbers + letters
print(funny)
print(lol)

x = [4, 2, 1]
dir(x)
trial = [n*2 for n in x]
print(trial)

# Nested Lists - Lists inside other lists

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[2][1])  # access 8


# printing values or interating through nest lists
# you need to use two loops
for x in nested_list:
    for val in x:
        print(val)

# prints  1,2,3,4,5,6,7,8,9

coords = [[10.423, 9.132], [37.212, -14.092], [21.367, 32.572]]
for location in coords:
    for coord in location:
        print(coord)


# creating a game board
board = [[num for num in range(1, 5) for val in range(1, 5)]]

print(board)  # [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]

lmao = [["x" if num % 2 != 0 else "O" for num in range(
    1, 5)] for val in range(1, 5)]
print(lmao)


# Enumerate
my_list = ["apples", "pears", "oranges", "fruits"]


# keeping track of an element and an index - HOWEVER, enumerate solves this issue!
count = 0
for element in my_list:
    print(element)
    if count == 1:
        print("Count is 1")
    count += 1

# 2nd way of keeping track of an element and an index

for x in range(len(my_list)):
    print(my_list[x])
    if x == 1:
        print("X is 1")

# Use Enumerate to not only loop through the index but also the element as well.

for x, element in enumerate(my_list):
    print(x, element)
    if x == 1:
        print("x is 1")


def dup_string(aString):
    newString = ""
    for char in aString:
        newString += char * 2
    return newString


print(dup_string("The"))


def dup_string(aString, value):
    newString = ""
    for char in aString:
        newString += char * value
    return newString


dup_string("Hello", 3)
