# if else problem
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 !=0 or n % 2 == 0 and n in range(6,20):
        print("Weird")
    elif (n % 2 == 0 and n in range(2,5)):
        print("Not Weird")
    else:
        print("Not Weird")



# function problem
def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 == 0:
        return  False
    else:
        return False        
    return leap

year = int(input())
