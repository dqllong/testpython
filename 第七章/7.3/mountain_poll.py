sandwich_orders = ['jirouwei', 'pastrami', 'pastrami', 'dacong', 'pastrami', 'jianbing']
finished_sandwiches = []
print("Pastrami saled!")
print(sandwich_orders)
#删除’pastrami'
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


while sandwich_orders:
    current_order = sandwich_orders.pop()

    print("I made your " + current_order + " sandwich.")
    finished_sandwiches.append(current_order)

print("The following are finished:\n\t")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)

print(sandwich_orders)

