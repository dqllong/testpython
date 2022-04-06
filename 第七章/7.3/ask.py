
responses = {}

active = True

while active:
    ask = input("what's your name? ")
    place = input("If you could visit one place in the world,where would you go? ")

    responses[ask] = place
    print(ask + " want to go to the " + place + ".")
    repeat = input("Somebody else? (yes/no)")

    if repeat == 'yes':
        active = True
    else:
        active = False

print(responses)
