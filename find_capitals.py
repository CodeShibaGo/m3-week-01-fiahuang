word = input("請輸入一個英文字或一句英文")

def find_capitals(word):

    #目標：找出大寫英文
    # list + isupper
    capitals = [char for char in word if char.isupper()]
    result = ''.join(capitals) #把for迴圈的字串再組合回去
    return result
    pass


result_capitals = find_capitals(word)
print(result_capitals)
