number = eval(input(""))
number_4 = (number // 1000) ** 4
number_3 = ((number % 1000) // 100) ** 4
number_2 = ((number // 10) % 10) ** 4
number_1 = (number % 10) ** 4
numbers = number_4 + number_3 + number_2 + number_1
if numbers == number:
    print("是四叶玫瑰数。")
else:
    print("不是四叶玫瑰数。")