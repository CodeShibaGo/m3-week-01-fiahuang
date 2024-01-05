list = [1.7, 5, 90, 63, 78, 42, 51, 0.6, 1.1, 0.5, -100, -1.3, -550, -1]
# list2 = [0,0,0]

# 第一步：篩選掉具有小數點的數字
# 用列表推導式直接建立新的列表
list_int = [int(x) for x in list if x.is_integer()]
print(list_int)

# 第二步：用第一步的結果選出最小的

def min_filter(list):
    print(min(list))


min_filter(list_int)
