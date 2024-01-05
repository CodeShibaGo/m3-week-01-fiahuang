def change_case(input_str, case):
    str_case = ""
    if case == "lower":
        str_case = input_str.lower()
    elif case == "upper":
        str_case = input_str.upper()
    return str_case