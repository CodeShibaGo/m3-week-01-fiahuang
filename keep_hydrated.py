# 喝水功能

#


import math

time = float(input("請輸入目前喝水間隔的時間是幾小時？"))

def litres(time):
    print(math.floor(time * 0.5))
    pass

litres(time)