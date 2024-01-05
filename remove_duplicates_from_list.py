seq_input = input("請輸入一個英文單字或一句英文：")

def distinct(seq_input):
    seq_list = list(seq_input)
    for x in seq_list:
        if seq_list.count(x) > 1:
            seq_input = seq_input.replace(x, "")
    return seq_input
    pass
result = distinct(seq_input)
print(result)