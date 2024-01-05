arr = [13,58,-51,12,1,-21,100]


def positive_sum(arr):
    positive_num = []
    for num in arr:
        if num > 0:
            positive_num.append(num)

    print(sum(positive_num))


positive_sum(arr)