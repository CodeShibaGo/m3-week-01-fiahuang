text = input("請輸入一個英文或一句英文：").lower() # 不區分大小寫的防呆

def count_duplicates(text):
    # 目標：確認重複，和重複的共有幾組
    # if條件句；出現重複+1，原本沒有=1（之後有就會+1）
    # list()：把字串拆成一個一個
    # dictionary: 把重複的字跟重複幾次搭成一組


    # 先刪除text中可能出現的空格
    text_nospace = text.replace(" ","")

    # 把text_nospace切分成一個一個字元，list建立可包含重複字元的新列表
    char = list(text_nospace)
    print(char)

    repeat_dict = {}
    char_count = 0
    for x in char:
        if char.count(x) > 1:
            char_count += 1
            repeat_dict[x] = repeat_dict.get(x, 0) + 1
            # 取得鍵 x 對應的值，如果 x 不在字典中（第一次遇到某字元），則返回預設值 0
            # 這行程式碼將字典中鍵 x 的值更新為原值（如果存在，由 get 取得儲存的值；不存在則直接預設0開始計算），加上 1。這樣做是為了紀錄每個字元重複的次數
    return char_count, repeat_dict

    pass

result_count, result_dict = count_duplicates(text)
# 因為該函式return兩個資料出來（char_count, repeat_dict），根據對應的前後順序位置設置變數


for char, count in result_dict.items():
    print(f"{char}: {count} 次")