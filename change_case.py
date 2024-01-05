user_input = input("請輸入字串：")
case = input("請輸入大寫upper或小寫lower：")

def change_case(input_str, case):
    str_case = ""
    if case == "lower":
        str_case = user_input.lower()
    elif case == "upper":
        str_case = user_input.upper()
    return str_case
    pass

case_change = change_case(user_input, case)
print(case_change)