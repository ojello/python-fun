# All the beginner material
# of python

# Variables and Data Types
# int
# str 'omo', "Jack", '1';
# bool, True, False - Only capitals
# float 0.32, 1.232

# variable
# declaring variable in python is writing it and setting it equal to something
# name = 'Tim'
# print(name)

# **variable names can contains underscores, text, and can't start with number, Capitals**

# NAME = 2
# name = 2
# NAME and name are not the same thing because
# Capitals matter in python


# print('Hello, What is your name?')
# prompts the user for an input
# name = input()
# print(name)

# 4 basic operators
# +
# -
# /
# *
# % modulos

# num1 = 3
# num2 = 45
# print(num1 + num2)

# print(num1 - num2)

# print(num1 * num2)

# exponent
# print(num1 ** num2)

# one division sign / - 6.4
# print(64 / 10)

# two division sign // - 6
# print(64 // 10)

# modulos - gives remainder
# 5 % 2
# remainder 3

# num3 = num1 ** num2
# print(num3)

# print('pick a number: ')
# num1 = input()
# print('Pick Another Number: ')
# num2 = input()
# total = int(num1) + int(num2)

# print('The amount is:', total)

# Conditions
# <
# >
# ==
#!=

# 18 > 10

# one equal sign is meant for declaration

# two equal sign is meant for comparison
# false
# print(5 == '5')

# if else statements
# if condition == True:
# do this

# age = input('Input your age:')
# if int(age) == 16:
#     print('you are 16 :D')
# elif int(age) > 16:
#     print('you are older than 16')


# height = input('put your height in:')

# if int(height) < 1:
#     print('you cannot ride')
# elif int(height) > 2:
#     print('you cannot ride, over 2m')
# else:
#     print('you can ride')

# # Chained Conditionals
# # uses and or and not
# x = 2
# y = 3

# if x == y and x + y == 5:
#     print('wow')

# if x == y or x + y == 5:
#     print('wow')

# if not(y == x or x + y == 5):
#     print('lol')
# else:
#     print(':(')


# # Nested If statements
# if m == 2:
#     if d == 4:
#         print('m = 2, y = 4')
#     else:
#         print('m = 2, y != 4')
# else:
#     print('x != 2')

# For loops
# for x in range(0, 10, 1):  # start, stop, stop
#     print(x)
# adding 1 to the variable x
# doesn't print 10 because it has to be less than 10

# # While Loops
# # while condition == True:
# # do this
# # keeps going when condition is true till the condition is false
# loop = True
# while loop:
#     name = input('insert something:')
#     if name == 'stop':
#         loop = False
#         break

# # Lists and Tuples
# # lists can be a collection of data types - same data types or different ones

# fruits = ['apple', 'pear', 3]
# print(fruits)

# # print out just pear
# print(fruits[1])

# # add an element to the list
# fruits.append('orange')

# fruits[3] = 'blueberry'
# print(fruits)
# # changes orange to blueberry
# # lists are useful to storing a lot of items

# # Tuple
# # used for coordinates, colors
# # looks very similar to a list,
# position = (2, 3)
# color = (255, 255, 255)
# print(type(color))

# Iteration by item

# # iterating through every item
# foods = ['spaghetti', 'cupcake', 'turnip']

# for food in foods:
#     print(food)
#     # will print each item from the foods list


# for food in foods:
#     if food == 'pears':
#         print(food)
#     else:
#         print('no pears')
# # checks every item to see if condition pears is true

# for x in range(0, len(foods)):
#     if food[x] == 'pears':
#         print(food[x])
#     else:
#         print('Not pears')

# String methods
# .strip(), len(), .lower(), .upper(), .split()
