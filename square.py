import math

n = int(input("請輸入一個整數："))

def is_square(n):

    # 分兩階段執行
    # 第一：開根號
    num = math.sqrt(n)

    # 第二：開根號之後是否為整數(aka 是平方數）
    if num.is_integer():
        print("True")
        return True
    else:
        print("False")
        return False
    pass


is_square(n)