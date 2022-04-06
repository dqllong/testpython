age = input("How old are you?")
age = int(age)
age = 0 < age < 100
while age < 3:
    print("Price:Free!")
    break
while 3 <= age <= 12:
    print("Price:10$")
    break
while age >= 12:
    print("Price:15")
    break