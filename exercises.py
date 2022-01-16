# 1Conditionals: Chapter 3

# 3.1
# Rewerite your pay computation to give the employee 1.5 times the hourly rate for hours worked aboved 40 hours.

# hr = float(input("Please enter hours: "))
# rate = float(input("Please enter rate: "))
# pay = hr * rate

# print("Pay: " + str(pay))

# 3.12
# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.
# ex. Enter Hours: 20 Enter Rate: nine --> return Error please enter numeric input.

hour = input("please enter hours: ")
rate = input("please enter rate: ")

# what gives you the ability to be so creative and display creativity in an artistic way --> through numbers and logic. allows you to express how you think without needing to be artistically talented.
try:
    val = float(hour)
    val2 = float(rate)
except:
    val = -1
    val2 = -1

if val > 0 and val2 > 0:
    print(rate * hour)
else:
    print("Error")

# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

score = input("Please enter score: ")
try:
    score = float(score)
except ValueError:
    print("Score must be a number. ")
    sys.exit()
if 0 <= score <= 1:
    if score >= .9:
        print("A")
    elif score >= .8:
        print("B")
    elif score >= .7:
        print("C")
    elif score >= .6:
        print("D")
    else:
        print("F")
else:
    print("Score must be between 0 and 1. ")

# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.
hrs = float(input("enter hours "))
rate = float(input("enter rate "))
pay = hrs * rate
bonus = 1.5
bs_hrs = 40

if hrs > 40.0:
    amt = ((hrs - 40) * (rate * bonus) + (bs_hrs * rate))
    print(amt)
else:
    amt = hrs * rate
    print(amt)
# 4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.
bonus = 1.5
h_limit = 40
h = float(input("enter hours: "))
r = float(input("enter rate: "))


def computepay(h, r):
    if h > 40.0:
        bonus_pay = (h - h_limit) * (r * bonus) + (h_limit * r)
        return str(bonus_pay)
    else:
        pay = h * r
        return str(pay)


p = computepay(45, 10.5)
print("Pay ", p)


# Leap Year Problem
def is_leap(year):
    leap = False

    # Write your logic here
    return leap


year = int(input())
print(is_leap(year))

# List Comprehension
# List comprehension - has expression followed with for loops and if clauses

# List Comprehension format:                                             [expression *for* value *in* collection]
# [expression *for* value *in* collection if <test>]

# the expression is in the list only if the if statements are true
# [expression *for* value *in* collection if <test1> and <test2>]

# [expr for val1 in collection1 and val2 in collection2]

# list of squares
# of first 100 integers

squares = []
for i in range(1, 101):
    squares.append(i**2)
print(squares)

# list comprehension example
squares2 = [i**2 for i in range(1, 101)]
print(squares2)

# finding the remainders
# finds the remainder of (x)^2 / 5
remainders5 = [x**2 % 5 for x in range(1, 101)]
print(remainders5)

# list of movies - finding the movies with the letter "G"
movies = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption", "Toy Theory", "Gone with the Wind",
          "Citizen Kane", "It's a Wonderful Life", "Wizard of Oz", "Gattaca", "Rear Window", "Ghost busters"]

# finding the movies that start with the letter "G" without list Comprehension.
movies = []
for title in movies:
    if title.startswith("G"):
        gmovies.append(title)

# Finding the movies that start with letter "G" using List Comprehension.

GMovies = [title for title in movies if title.startswith("G")]
print(GMovies)

# Movies with year
movies2 = [("Citizen Kane", 1941), ("Spirited Away", 2001), ("It's a Wonderful Life", 1946),
           ("Gattaca", 1997), ("No Country for Old Men", 2007), ("Rear Window", 1945), ("The Lord of the Rings", 1997), ("Cat away", 1992), ("Tomb Raiders", 2000), ("Exodus", 2000), ("Tom and Jerry", 1997), ("Maya", 1921)]

pre2000 = [title for (title, year) in movies2 if year < 2000]
print(pre2000)

# scalar multiplication with list comprehension

v = [4, -3, 1]
w = [4*x for x in v]
print(w)  # prints 8,-12,4


# Use list comprehension to compute the Cartesian Product of each set.

# If A and B are sets, then the cartesian product is the set of pairs (a, b) where "a" is in A and "b" is in B
# A = {1,3}
# B = {x, y}
# A x B = { (1,x), (1,y), (3,x), (3,y)}

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)


# substring = ""
# fullstring = []
# def count(substring, fullstring):
#     count = sum(substring in x for x in fullstring)

# print(count)


pets = [("Ivy", 12), ("Graham", 1), ("Ming", 3), ("Oli", 3),
        ("Odette", 4), ("Lily", 5), ("Lady", 2)]

petsage = [name for (name, age) in pets if age <= 12]
print(petsage)


A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)


x = int(input())
y = int(input())
z = int(input())
n = int(input())


test = [[i, j, k] for i in range(x + 1) for j in range(y + 1)
        for k in range(z + 1) if i + j + k != n]
print(test)


# range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default) and stops before a specified number.

# start - optional - an integer number specifying at which position to start
# stop - required, an integer number specifying at which position to stop (not included)

# step - optional - an integer number specifying the incrementation. Default is 1.

# range(start, stop, step)
x = range(3, 6)
for n in x:
    print(n)  # outputs 3,4,5


# creates a sequence of numbers from 3 to 19, but increment by 2 instead of 1.
x = range(3, 20, 2)
for n in x:
    print(n)

# Nested lists

# store student names and grades in a nested list and print the names of any students having the second lowest grade.

# if there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line


# students = [[]]


# Nested List practice
# rank = [name for (name, grade) in students students.sort() if grade[]= students[1]]

name = input("name: ")
grade = float(input("grade: "))
classroom = [[name, grade]]

for (name, grade) in classroom:
    classroom = [[name, grade]]

 [name for (name, grade) in classroom if classroom[x][0] < class[0][0]]


# length = len(students)
# students.sort()
# for name in (name, grade) in students:
#     if


pets = [("Ivy", 12), ("Graham", 1), ("Ming", 3), ("Oli", 3),
        ("Odette", 4), ("Lily", 5), ("Lady", 2)]

petsage = [name for (name, age) in pets if age <= 12]
print(petsage)


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






