# if else problem

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0 or n % 2 == 0 and n in range(6, 21):
        print("Weird")
    elif (n % 2 == 0 and n in range(2, 5)):
        print("Not Weird")
    else:
        print("Not Weird")


# division problem
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a/b)


# arithmetic problem
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)


# function problem
def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 == 0:
        return False
    else:
        return False
    return leap


year = int(input())


# loops problem

def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 == 0 or year % 4 != 0:
        return False
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return True
    return leap


year = int(input())
print(is_leap(year))
# test 5 - 1992
# test 1 - 2100
