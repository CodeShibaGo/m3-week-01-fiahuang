first_name = input("請輸入英文名：")
last_name = input("請輸入英文姓：")

def abbrev_name(first_name, last_name):

    #目標：取姓跟名的第一個字（大寫）組合成縮寫
    #list + capitalize + join
    firstname_list = list(first_name.capitalize())
    lastname_list = list(last_name.capitalize())
    print(f"{firstname_list[0]}.{lastname_list[0]}")

    pass

abbrev_name(first_name, last_name)
