import random

try:
    n_friends = int(input('Enter the number of friends joining (including you):\n'))
except ValueError:
    print("invalid input")
else:
    if n_friends > 0:
        print()
        print('\nEnter the name of every friend (including you), each on a new line:')
        friends = {input(): 0 for _ in range(n_friends)}
        bill = int(input('\nEnter the total bill value:\n'))
        use_lucky = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
        if use_lucky == 'Yes':
            random.seed()
            lucky_one = random.choice(list(friends.keys()))
            print(f'\n{lucky_one} is the lucky one!')
            friends = dict.fromkeys(friends, round(bill / (n_friends - 1), 2))
            friends[lucky_one] = 0
        else:
            print('\nNo one is going to be lucky')
            friends = dict.fromkeys(friends, round(bill / n_friends, 2))
        print()
        print(friends)
    else:
        print("No one is joining for the party")
