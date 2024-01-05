user_input = input("請輸入字串：")

def reverse_string(s):
    reversed_str = "" # 空字串等等for迴圈存放用
    for character in s:
        reversed_str = character + reversed_str
    return reversed_str
    pass

reversed_input = reverse_string(user_input)
print(reversed_input)



