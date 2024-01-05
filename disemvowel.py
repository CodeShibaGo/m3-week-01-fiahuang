str = input("請輸入一個英文單字或一句英文：")

def disemvowel(str):
    # 目標：刪除母音aeiou
    # 用list、replace、for迴圈
    vowel_list = ['a','e','i','o','u']
    str_list = list(str)
    for x in vowel_list:
        str = str.replace(x,"")
    return str

    pass

result = disemvowel(str)
print(result)