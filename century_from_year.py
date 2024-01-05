import math

year = input("請輸入要轉換的年份：")

def century(year):
    year_convert = math.ceil(int(year)/100)
    print(year_convert)
    pass


century(year)