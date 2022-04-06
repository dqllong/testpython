x = 1
while x <= 5:
    print(x)
    x += 1
prompt = "You can add your pizza here! "
order = ""

while order != 'quit':
    order += input(prompt)
    order += ","

    print("You can add more,and we add these for you:" + order)


