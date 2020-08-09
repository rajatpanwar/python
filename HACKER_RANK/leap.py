def is_leap(n):             //define the function
    if n % 400 == 0:
        return True
    if n % 100 == 0:              #condition for leap year
        return False
    if n % 4 == 0:
        return True
    return False



year = int(input())       //take input from user
print(is_leap(year))
