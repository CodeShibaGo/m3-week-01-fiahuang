def positive_sum(arr):
    positive_num = []
    for num in arr:
        if num > 0:
            positive_num.append(num)

    return sum(positive_num)
