def oddEven(number):
    if number % 2 == 1:
        print(f"數字{number}為奇數")
    elif number % 2 == 0:
        print(f"數字{number}為偶數")

number = int(input("請輸入一個數字："))

oddEven(number)