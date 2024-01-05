sheep = [True, True, True, False, True]

def count_sheep(sheep):

    #目標：計算true的數量

    sleep_count = 0
    sheep_list = list(sheep)
    print(sheep_list)
    for x in sheep_list:
        if x == True:
            sleep_count +=1
    print(sleep_count)

    pass


count_sheep(sheep)