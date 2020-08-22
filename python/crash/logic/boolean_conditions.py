alien = 'black'

if alien == 'green':
    print('You have earned 5 points')
elif alien == 'yellow':
    print('You have earned 10 points')
elif alien == 'red':
    print('You have earned 15 points')

usernames = ['henry', 'bonner', 'mozambique', 'normal']

for user in usernames:
    if user == 'bonner':
        print(f"You now have command, {user}.")
    else:
        print(f"Hello, {user.title()}... Welcome to your initiation.")

newusers = ['rally', 'normal']

for newuser in newusers:
    if (newuser in usernames):
        print(f"\nI'm terribly sorry, {newuser}, but you already seem to be in our system")
    else:
        print(f"Welcome, {newuser}")
