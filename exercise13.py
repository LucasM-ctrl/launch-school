user = input('What is your name? ')

if '!' in user:
    print(f'HELLO {user.upper()} WHY ARE WE YELLING?')
else:
    print(f'Hello {user}.')