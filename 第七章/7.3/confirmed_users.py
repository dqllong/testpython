#创建列表

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user.title())

print("\nThe following users have been confirmed：\n\t")
for confirmed_user in confirmed_users:
    print(confirmed_user)