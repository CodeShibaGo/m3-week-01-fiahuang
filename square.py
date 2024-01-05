import math

def is_square(n):
    num = math.sqrt(n)
    if num.is_integer():
        print("True")
        return True
    else:
        print("False")
        return False