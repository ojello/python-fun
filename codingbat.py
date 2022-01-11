# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True

def sleep_in(weekday, vacation):
    if not weekday and vacation:
        return True
    elif not weekday and not vacation:
        return True
    elif weekday and vacation:
        return True
    else:
        return False

# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False


def monkey_trouble(a_smile, b_smile):
    if (a_smile and b_smile) or (not a_smile and not b_smile):
        return True
    else:
        return False

# Given two int values, return their sum. Unless the two values are the same, then return double their sum.

# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8


def sum_double(a, b):
    if(a == b):
        return ((a*2) + (b*2))
    else:
        return (a + b)


# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0
def diff21(n):
    if n > 21:
        return abs(21-n)+abs(21-n)
    else:
        return abs(21-n)


# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

# parrot_trouble(True, 6) → True
# parrot_trouble(True, 7) → False
# parrot_trouble(False, 6) → False
def parrot_trouble(talking, hour):
    if talking and 6 <= hour > 20:
        return True
    elif talking and hour == 6:
        return True
    else:
        return False


# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


# makes10(9, 10) → True
# makes10(9, 9) → False
# makes10(1, 9) → True

def makes10(a, b):
    if (a + a) == 10 or (b + b) == 10:
        return True
    elif a == 10 or b == 10:
        return True
    elif (a + b) == 10:
        return True
    else:
        return False


# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.


# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False


def near_hundred(n):
    if 90 <= n <= 110 or (190 <= n <= 210):
        return True
    else:
        return False


# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;


# front_times('Chocolate', 2) → 'ChoCho'
# front_times('Chocolate', 3) → 'ChoChoCho'
# front_times('Abc', 3) → 'AbcAbcAbc'
def front_times(str, n):
    if n > 0:
        return str[0:3]*n
    elif n == 0:
        return ""
    else:
        return str


# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello'


# skipping characters


def test(s):
    for index, char in enumerate(s):
        if index % 2 == 0:
            return char


test("Hello")


def test2(m):
    for index, char in enumerate(m):
        print(char)
        return char

# for i in str:

# so i here is a character in str (you should probably use a different variable name, as str is a reserved word).  You don't need i += 1 because the for loop will naturally progress to the next character.  All you have to do is break from the while and the for loop will go to the next letter
# seems like you only need for OR while and not both
# You're trying to do similar things with both
# Why don't you try a for idx, letter in enumerate(mystr):


# Given a string, return a string where for every char in the original, there are two chars.


# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'

def dup_string(aString):
    newString = ""
    for char in aString:
        newString += char * 2
    return newString


print(dup_string("The"))


# Return the number of times that the string "hi" appears anywhere in the given string.


# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2

def count_hi(str):
    return str.count("hi")


# Return True if the string "cat" and "dog" appear the same number of times in the given string.


# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(str):
    if str.count("dog") == str.count("cat"):
        return True
    else:
        return False


# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2

def count_code(str):
    replace =
    return str.count("code") or str.:


def end_other(a, b):
    if (a.upper() or a.lower()) in (b):
        return True
    elif (b.upper() or b.lower()) in (a or b):
        return True
    else:
        return False

# count_evens
# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            count += 1
    return count


# big_diff
# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.


# big_diff([10, 3, 5, 6]) → 7
# big_diff([7, 2, 10, 9]) → 8
# big_diff([2, 10, 7, 2]) → 8
def big_diff(nums):
    difference = max(nums) - min(nums)
    return difference


# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.


# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3
