b = input("請輸入True或False：").lower()

def boolean_to_string(b):
    if b == "true":
        print("True")
        return True
    elif b == "false":
        print("False")
        return False
    pass


boolean_to_string(b)