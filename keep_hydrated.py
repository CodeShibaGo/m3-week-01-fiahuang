# 喝水功能

# 每小時喝200ml，小時取整數，每滿一個小時才加一次0.5（不足1都捨去）

import math

time = float(input("請輸入目前喝水間隔的時間是幾小時？"))

def litres(time):
    print(math.floor(time * 0.5))
    pass

litres(time)