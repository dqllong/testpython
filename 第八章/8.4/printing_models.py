unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:

    print("Printing model: " + unprinted_designs.pop())
    completed_models.append(unprinted_designs.pop())

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
