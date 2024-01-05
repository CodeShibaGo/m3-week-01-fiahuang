def array_diff(a, b):
    #目標：兩個列表，有重複的元素就槓掉
    result = list(set(a) - set(b))

    print(result)

    pass